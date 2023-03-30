import scrapy
import time
from crawlers.utils import format_metro_product

class MetroSpider(scrapy.Spider):
  handle_httpstatus_list = [403, 429]
  name = 'metro'
  allowed_domains = ['metro.ca']
  start_urls = ['https://www.metro.ca/en/online-grocery/search']
  
  custom_settings = {
    'DOWNLOAD_DELAY': 25,
    'AUTOTHROTTLE_START_DELAY': 25,
    'CONCURRENT_REQUESTS': 1,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
  }
  
  def __init__(self, *args, **kwargs):
    super(MetroSpider, self).__init__(*args, **kwargs)
    self.storeType = 'Metro'
    self.storeId = '0000'
    self.count = 0
          
  def parse(self, response):
    for product in response.css('div.default-product-tile'):
      self.count += 1
      if self.count % 100 == 0:
        print(f'Parsed {self.count} products...')
      
      image_container = product.css('picture.defaultable-picture')
      normalized_price_container = product.css('div.pricing__secondary-price')
      
      sku = product.css('div.default-product-tile::attr(data-product-code)').get()
      category = product.css('div.default-product-tile::attr(data-product-category)').get()
      brand = product.css('span.head__brand::text').get()
      brand = brand.strip('\r\n ') if brand else ''
      image_url = image_container.css('img::attr(src)').get()
      name = product.css('div.head__title::text').get()
      packageSize = product.css('span.head__unit-details::text').get()
      price = product.css('span.price-update::text').get()
      normalized_price = normalized_price_container.css('span::text').get()
      unit = normalized_price_container.css('abbr::text').get()
      parentCompany = 'Metro'
      
      
      if normalized_price is not None and unit is not None:
        normalized_price = normalized_price + unit
      
      product = {
        'name': name,
        'SKU': sku,
        'brand': brand,
        'category': category,
        'imageUrl': image_url,
        'packageSize': packageSize,
        'parentCompany': parentCompany,
        'price': price,
        'normalizedPrice': normalized_price,
      }
      
      product = format_metro_product(product)
      yield product
    
    # follow pagination links (should be about 700 pages)
    pagination_container = response.css('div.product-page-nav')
    next_page_url = pagination_container.xpath('.//a[contains(., "Next")]/@href').get()
    if next_page_url is not None:
      base_url = 'https://www.metro.ca'
      next_page_url = base_url + next_page_url
      yield response.follow(next_page_url, self.parse)
  

