import scrapy
import json
import time
from scrapy.http.request.json_request import JsonRequest
from crawlers.data import loblaws_categories
from crawlers.items import ProductItem
from crawlers.utils import format_loblaws_product

class LoblawsSpider(scrapy.Spider):
  name = 'loblaws'
  allowed_domains = ['api.pcexpress.ca', 'pcexpress.ca']
  
  custom_settings = {
    'CONCURRENT_REQUESTS': 16,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 16,
    'DOWNLOAD_DELAY': 3,
    'AUTOTHROTTLE_START_DELAY': 3
  }
  
  base_request_body = {
    "lang": "en",
    "pickupType": "STORE",
    "date": time.strftime("%d%m%Y"),
    "offerType": "ALL",
    "cartId": "c807d16d-1138-4236-b555-c90793f37353",
  }
  
  request_headers = {
    "Content-Type": "application/json",
    "x-apikey": "1im1hL52q9xvta16GlSdYDsTsG0dmyhF"
  }
  
  
  def start_requests(self):
    if self.storeId is None or self.storeType is None:
      raise ValueError("Missing storeId or storeType parameters")
    
    print(f'Fetching products for store {self.storeId} ({self.storeType})...')
    print(f'firestoreId: {self.firestoreId}')
    
    for key in loblaws_categories:
      request_body = {
        **self.base_request_body,
        "storeId": self.storeId,
        "banner": self.storeType,
        "categoryId": loblaws_categories.get(key),
        "pagination": {
          "from": 0,
          "size": 48
        }
      }

      yield JsonRequest(
        url='https://api.pcexpress.ca/product-facade/v3/products/category/listing',
        method='POST',
        headers=self.request_headers,
        data=request_body,
        callback=self.parse_category,
        cb_kwargs=dict(category=key, page=0)
      )
  

  def parse_category(self, response, category, page):
    print(f'Parsing category {category} page {page + 1}...')
    json_response = json.loads(response.text)
    
    totalResults = json_response['pagination']['totalResults']
    print(f'Found {totalResults} products for category {category}')
    
    products = [format_loblaws_product(p) for p in list(json_response['results'].values())]
    products = [p for p in products if p is not None]
    
    for product in products:
      try:
        product_item = ProductItem(product)
        yield product_item
      except Exception as e:
        print(f'Error parsing product {product["name"]}')
        print(e)
    

    if page == 0:
      maxPage = totalResults // 48
      
      for p in range(1, maxPage + 1):
        print(f'Fetching page {p} of {maxPage} for category {category}...')
        
        request_body = {
          **self.base_request_body,
          "storeId": self.storeId,
          "banner": self.storeType,
          "categoryId": loblaws_categories.get(category),
          "pagination": {
            "from": p,
            "size": 48
          }
        }
        
        yield JsonRequest(
          url='https://api.pcexpress.ca/product-facade/v3/products/category/listing',
          method='POST',
          headers=self.request_headers,
          data=request_body,
          callback=self.parse_category,
          cb_kwargs=dict(category=category, page=p)
        )
  
