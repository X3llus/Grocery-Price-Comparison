from urllib.parse import urlencode
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
    storeId = getattr(self, 'storeId', None)
    if storeId is None:
      print('Store ID not provided. Using default store ID of 3153 (Orillia, ON).')
      self.storeId = 3153
    
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
    products = [format_base_product(p) for p in list(json_response['items']['products'].values())]
    productsToFetch = json_response['items']['productsToFetch']
    
    data = { 'lang': 'en', 'products': productsToFetch }
    yield JsonRequest(url='https://www.walmart.ca/api/bsp/fetch-products?experience=grocery', method='POST', data=data, callback=self.parse_additional_products, cb_kwargs=dict(products=products, category=category))

    if page == 1:
      maxPage = totalResults // pageSize
      # limiting to 5 pages for now (300 products per category)
      if maxPage > 5:
        maxPage = 5
      
      for p in range(2, maxPage + 1):
        print(f'Fetching page {page} of {maxPage} ({round(page / maxPage * 100, 2)}%)')
        payload = { 'experience': 'grocery', 'lang': 'en', 'c': walmart_categories[category], 'p': p }
        url = 'https://www.walmart.ca/api/bsp/browse?' + urlencode(payload)
        yield scrapy.Request(url=url, callback=self.parse_category, cb_kwargs=dict(category=category, page=p))
    
  
  def parse_additional_products(self, response, products, category):
    json_response = json.loads(response.text)
    additionalProducts = [format_base_product(p) for p in list(json_response['products'].values())]
    products.extend(additionalProducts)
    
    priceRequestData = get_price_request_body(products, self.storeId)
    yield JsonRequest(url='https://www.walmart.ca/api/bsp/v2/price-offer', method='POST', data=priceRequestData, callback=self.parse_prices, cb_kwargs=dict(products=products, category=category))
  
  
  def parse_prices(self, response, products, category):
    json_response = json.loads(response.text)
    prices = [trim_price_response(p) for p in list(json_response['offers'].values())]
    
    for product in products:
      if len(product['SKU']) == 0:
        sku = 'N/A'
      else:
        sku = product['SKU'][0]
      price = next((p for p in prices if p['sku'] == sku), None)
      if price is not None:
        productData = {
          'name': product['name'],
          'brand': product['brand'],
          'category': category,
          'imageUrl': product['imageUrl'],
          'packageSize': product['packageSize'],
          'price': price['price'],
          'normalizedPrice': price['normalizedPrice'],
          'SKU': sku,
          'dateExtracted': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        try:
          productItem = ProductItem(productData)
          yield productItem
        except Exception as e:
          print(e)
    
    
  
