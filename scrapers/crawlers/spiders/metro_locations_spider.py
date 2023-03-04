import scrapy
from dotenv import dotenv_values
import aiohttp

class MetroLocationsSpider(scrapy.Spider):
  config = dotenv_values('C:\Lakehead\Winter2023\COMP4431-AdvancedProject\Grocery-Price-Comparison\scrapers\.env')
  access_token = config.get('MAPBOX_ACCESS_TOKEN')
  name = 'metro_locations'
  allowed_domains = ['fresh2go.metro.ca']
  start_urls = ['https://fresh2go.metro.ca/storepickup']
  
  
  
  async def parse(self, response):
    store_table = response.css('div.result_store').xpath('.//table')
    
    for store in store_table.xpath('(.//tr)/td[1]'):
      store_data = store.xpath('(.//text())').getall()
      store_data = [x.strip() for x in store_data if x.strip() != '']
      if len(store_data) == 0:
        continue
      
      store_id = store_data[0].split('-')[1].strip()
      line1 = store_data[1].strip()
      town = store_data[2].strip()
      region = store_data[3].strip()
      country = store_data[4].strip()
      type = 'Metro'
      
      if len(store_data) > 0:
        async with aiohttp.ClientSession() as session:
          async with session.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{line1} {town}.json?access_token={self.access_token}&limit=1') as response:
            data = await response.json()
            if data.get('features'):
              formatted_address = data.get('features')[0].get('place_name')
              longitude = data.get('features')[0].get('center')[0]
              latitude = data.get('features')[0].get('center')[1]
              feature_context = data.get('features')[0].get('context')
              postal_code_context = [context for context in feature_context if context.get('id').startswith('postcode')]
              postal_code = postal_code_context[0].get('text') if postal_code_context else None
              
              yield {
                'storeId': store_id,
                'type': type,
                'address': {
                  'line1': line1,
                  'town': town,
                  'region': region,
                  'country': country,
                  'formattedAddress': formatted_address,
                  'postalCode': postal_code,
                  'geoPoint': {
                    'latitude': latitude,
                    'longitude': longitude
                  }
                }
              }

    