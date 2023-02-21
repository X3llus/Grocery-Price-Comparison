import time
import traceback

from typing import Dict
import asyncio
import aiohttp
from aiolimiter import AsyncLimiter

from data import categories
from utils import filter_unique_products, format_product
from RealtimeDbHelper import RealtimeDbHelper
from FirestoreHelper import FirestoreHelper


# The Orillia Zehrs
lat = 44.58857
lng = -79.415588

limiter = AsyncLimiter(max_rate=2, time_period=1) # 2 requests per second

request_headers = {
  "Content-Type": "application/json",
  "x-apikey": "1im1hL52q9xvta16GlSdYDsTsG0dmyhF"
}

base_request_body = {
  "storeId": "0559",
  "banner": "zehrs",
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
    try:
      data = await get_products(session, category, page)
      print(f"Fetching {category}. {len(products) + 48} / {data['pagination']['totalResults']} products fetched")
      
      # keep only the fields we need and remove products that don't have a SKU
      formatted_products = [format_product(product) for product in data['results']]
      formatted_products = [product for product in formatted_products if product is not None]
      
      products += formatted_products
    except:
      print(f"Error fetching {category} page {page}")
      print(traceback.format_exc())
      break

  print(f"{category} complete. {len(products)} products fetched")
  all_products.extend(products)


async def get_all_products() -> Dict:
  all_products = []
  async with aiohttp.ClientSession() as session:
    tasks = []
    for category in categories.keys():
      tasks.append(asyncio.create_task(get_products_for_category(session, category, all_products)))
    await asyncio.gather(*tasks)
  return all_products


def main():
  start_time = time.time()
  products = asyncio.run(get_all_products())
  
  # remove duplicate products. this occurs when a product is in multiple categories
  products = filter_unique_products(products)
  
  end_fetch_time = time.time()
  db = FirestoreHelper()
  store_type = 'zehrs'
  store_id = '0559'
  db.process_base_products(products, 'Loblaws')
  end_time = time.time()
  
  print(f'Fetch time: {end_fetch_time - start_time}')
  print(f'Process time: {end_time - end_fetch_time}')
  print(f'Total time: {end_time - start_time}')
  
    
main()