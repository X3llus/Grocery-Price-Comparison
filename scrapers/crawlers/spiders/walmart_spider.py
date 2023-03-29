from urllib.parse import urlencode
import scrapy
import json
from scrapy.http.request.json_request import JsonRequest
from crawlers.data import walmart_categories
from crawlers.items import ProductItem
from crawlers.utils import format_walmart_product, get_price_request_body, trim_price_response

class WalmartSpider(scrapy.Spider):
  name = 'walmart'
  allowed_domains = ['walmart.ca']
  
  custom_settings = {
    'RETRY_TIMES': 1
  }
  
  def start_requests(self):
    if self.storeId is None:
      raise ValueError("Missing storeId parameter")
    
    for key in walmart_categories:
      payload = { 'experience': 'grocery', 'lang': 'en', 'c': walmart_categories[key], 'p': 1 }
      url = 'https://www.walmart.ca/api/bsp/browse?' + urlencode(payload)
      yield scrapy.Request(url=url, callback=self.parse_category, cb_kwargs=dict(category=key, page=1))
  
  
  # The request loop is as follows:
  # 1. Hit /browse to get the first 15 products of a page as well as the total number of products and products per page
  # 2. Hit /fetch-products to get the dynamically loaded products for the page
  # 3. Hit /price-offer to get the price of each product on the page
  # 4. Repeat steps 1 - 3 with incremented page number until all pages have been fetched
  def parse_category(self, response, category, page):
    json_response = json.loads(response.text)
    
    totalResults = json_response['pagination']['totalResults']
    pageSize = json_response['pagination']['pageSize']
    print(f'Found {totalResults} products for category {category}')
    
    products = [format_walmart_product(p) for p in list(json_response['items']['products'].values())]
    products = [p for p in products if p is not None]
    
    productsToFetch = json_response['items']['productsToFetch']
    
    data = { 'lang': 'en', 'products': productsToFetch }
    yield JsonRequest(url='https://www.walmart.ca/api/bsp/fetch-products?experience=grocery', method='POST', data=data, callback=self.parse_additional_products, cb_kwargs=dict(products=products))

    if page == 1:
      maxPage = totalResults // pageSize
      
      # limiting to 6 pages for now (360 products per category)
      if maxPage > 6:
        maxPage = 6
      
      for p in range(2, maxPage + 1):
        print(f'Fetching page {p} of {maxPage} for category {category}...')
        payload = { 'experience': 'grocery', 'lang': 'en', 'c': walmart_categories[category], 'p': p }
        url = 'https://www.walmart.ca/api/bsp/browse?' + urlencode(payload)
        yield scrapy.Request(url=url, callback=self.parse_category, cb_kwargs=dict(category=category, page=p))
    
  
  def parse_additional_products(self, response, products):
    json_response = json.loads(response.text)
    
    additionalProducts = [format_walmart_product(p) for p in list(json_response['products'].values())]
    additionalProducts = [p for p in additionalProducts if p is not None]
    products.extend(additionalProducts)
    
    priceRequestData = get_price_request_body(products, self.storeId)
    yield JsonRequest(url='https://www.walmart.ca/api/bsp/v2/price-offer', method='POST', data=priceRequestData, callback=self.parse_prices, cb_kwargs=dict(products=products))
  
  
  def parse_prices(self, response, products):
    json_response = json.loads(response.text)
    
    prices = [trim_price_response(p) for p in list(json_response['offers'].values())]
    prices = [p for p in prices if p is not None]
    
    for product in products:
      if len(product['SKU']) == 0:
        continue
      else:
        sku = product['SKU'][0]
      price = next((p for p in prices if p['sku'] == sku), None)
      if price is not None:
        productData = {
          'name': product['name'],
          'brand': product['brand'],
          'imageUrl': product['imageUrl'],
          'packageSize': product['packageSize'],
          'price': price['price'],
          'normalizedPrice': price['normalizedPrice'],
          'SKU': sku,
        }
        try:
          productItem = ProductItem(productData)
          yield productItem
        except Exception as e:
          print(e)
    
    
  
