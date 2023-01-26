import scrapy
import json
from datetime import datetime
from scrapy.http.request.json_request import JsonRequest
from crawlers.data import walmart_categories
from crawlers.items import ProductItem
from crawlers.utils import format_base_product, get_price_request_body, trim_price_response

class WalmartSpider(scrapy.Spider):
  name = 'walmart'
  allowed_domains = ['walmart.ca']
  
  def start_requests(self):
    category = getattr(self, 'category', None)
    if category is None:
      raise ValueError('Category is required')
    if category not in walmart_categories:
      raise ValueError('Category is not valid. See data.py for valid categories.')
    
    storeId = getattr(self, 'storeId', None)
    if storeId is None:
      print('Store ID not provided. Using default store ID of 3153 (Orillia, ON).')
      self.storeId = 3153
      
    url = f'https://www.walmart.ca/api/bsp/browse?experience=grocery&lang=en&c={walmart_categories[category]}'
    yield scrapy.Request(url, self.parse)
  
  
  # The request loop is as follows:
  # 1. Hit /browse to get the first 15 products of a page as well as the total number of products and products per page
  # 2. Hit /fetch-products to get the dynamically loaded products for the page
  # 3. Hit /price-offer to get the price of each product on the page
  # 4. Repeat steps 1 - 3 with incremented page number until all pages have been fetched
  def parse(self, response):
    json_response = json.loads(response.text)
    totalResults = json_response['pagination']['totalResults']
    pageSize = json_response['pagination']['pageSize']
    products = [format_base_product(p) for p in list(json_response['items']['products'].values())]
    productsToFetch = json_response['items']['productsToFetch']
    
    data = { 'lang': 'en', 'products': productsToFetch }
    yield JsonRequest(url='https://www.walmart.ca/api/bsp/fetch-products?experience=grocery', method='POST', data=data, callback=self.parse_additional_products, cb_kwargs=dict(products=products))

    maxPage = totalResults // pageSize
    for page in range(2, maxPage + 1):
      print(f'Fetching page {page} of {maxPage} ({round(page / maxPage * 100, 2)}%)')
      url = f'https://www.walmart.ca/api/bsp/browse?experience=grocery&lang=en&c={walmart_categories[self.category]}&p={page}'
      yield scrapy.Request(url, self.parse)
    
  
  def parse_additional_products(self, response, products):
    json_response = json.loads(response.text)
    additionalProducts = [format_base_product(p) for p in list(json_response['products'].values())]
    products.extend(additionalProducts)
    
    priceRequestData = get_price_request_body(products, self.storeId)
    yield JsonRequest(url='https://www.walmart.ca/api/bsp/v2/price-offer', method='POST', data=priceRequestData, callback=self.parse_price, cb_kwargs=dict(products=products))
  
  
  def parse_price(self, response, products):
    json_response = json.loads(response.text)
    prices = [trim_price_response(p) for p in list(json_response['offers'].values())]
    
    for product in products:
      sku = product['skuIds'][0]
      price = next((p for p in prices if p['sku'] == sku), None)
      if price is not None:
        productData = {
          'name': product['name'],
          'brand': product['brand'],
          'imageUrl': product['imageUrl'],
          'packageSize': product['packageSize'],
          'price': price['price'],
          'normalizedPrice': price['normalizedPrice'],
          'dateExtracted': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        try:
          productItem = ProductItem(productData)
          yield productItem
        except Exception as e:
          print(e)
    
    
  
