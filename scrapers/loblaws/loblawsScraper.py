import json
import time
from typing import Dict
import asyncio
import aiohttp
from aiolimiter import AsyncLimiter

from data import categories, store_locations
from utils import get_closest_store, format_product, get_unique_products


# The Orillia Zehrs
lat = 44.58857
lng = -79.415588
closest_store = get_closest_store(lat, lng, store_locations)

limiter = AsyncLimiter(max_rate=2, time_period=1) # 2 requests per second

request_headers = {
  "Content-Type": "application/json",
  "x-apikey": "1im1hL52q9xvta16GlSdYDsTsG0dmyhF"
}

base_request_body = {
  "storeId": closest_store['id'],
  "banner": closest_store['storeBannerId'],
  "lang": "en",
  "pickupType": "STORE",
  "date": time.strftime("%d%m%Y"),
  "offerType": "ALL",
  "cartId": "c807d16d-1138-4236-b555-c90793f37353",
}


async def get_products(session, category: str, page: int = 0) -> Dict:
  request_body = {
    **base_request_body,
    "categoryId": categories.get(category),
    "pagination": {
      "from": page,
      "size": 48
    }
  }
  
  async with limiter:
    async with session.post("https://api.pcexpress.ca/product-facade/v3/products/category/listing", json=request_body, headers=request_headers) as response:
      data = await response.json()
      return data
  
  
async def get_products_for_category(session, category, all_products) -> Dict:
  page = 0
  products = []

  data = await get_products(session, category, page)
  print(f"Fetching {category}. Total products: {data['pagination']['totalResults']}")
  formatted_products = [format_product(product) for product in data['results']]
  products += formatted_products

  while len(products) < data['pagination']['totalResults']:
    page += 1
    data = await get_products(session, category, page)
    print(f"Fetching {category}. {len(products) + 48} / {data['pagination']['totalResults']} products fetched")
    formatted_products = [format_product(product) for product in data['results'] if product['stockStatus'] == "OK"]
    products += get_unique_products(formatted_products)

  print(f"{category} complete. {len(products)} products fetched")
  all_products[category] = products


async def get_all_products() -> Dict:
  all_products = {}
  async with aiohttp.ClientSession() as session:
    tasks = []
    for category in categories.keys():
      tasks.append(asyncio.create_task(get_products_for_category(session, category, all_products)))
    await asyncio.gather(*tasks)
  return all_products


def main():
  products = asyncio.run(get_all_products())
  file_path = "test-extraction-data.json"
  with open(file_path, "w") as outfile:
    json.dump(products, outfile, indent=4)
    
main()