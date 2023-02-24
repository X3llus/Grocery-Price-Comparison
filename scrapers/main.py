import time
import os
from FirestoreHelper import FirestoreHelper
from RealtimeDbHelper import RealtimeDbHelper
from crawlers.runner import run as scrapy_run

firestore_helper = FirestoreHelper()
realtimedb_helper = RealtimeDbHelper()

def main():
  start_time = time.time()
  
  # Get stores in radius around Orillia
  lat = 44.58857
  lng = -79.415588
  radius = 75
  
  stores = firestore_helper.get_local_stores(lat, lng, radius)
  num_stores = len(stores)
  print(f'\nFound {num_stores} stores within {radius}km of {lat}, {lng}.\n')
  
  scrapy_run(stores)
  
  print(f'\nAll stores complete. Total time: {time.time() - start_time} seconds.')


def get_data_for_store(store):
  type = str(store['type']).lower()
  print(f'Processing {type} store {store["storeId"]}')
  
  extraction_time = 0
  
  if type == 'walmart':
    company = 'walmart'
  else:
    company = 'loblaws'
  
  scraping_time = scrapy_run(company, str(store['storeId']), type)
  base_product_time = firestore_helper.process_base_products(type)
  prices_time = realtimedb_helper.process_product_prices(str(store['storeId']), type)
  
  extraction_time = scraping_time + base_product_time + prices_time
  
  if os.path.exists('product_items.jsonl'):
    os.remove('product_items.jsonl')

  
  print(f'\nFinished processing {type} store {store["storeId"]}.')
  print(f'Extraction time: {extraction_time} seconds.\n')
      
    
if __name__ == '__main__':
  main()