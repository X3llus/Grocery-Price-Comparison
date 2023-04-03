import time
import random
from FirestoreHelper import FirestoreHelper
from crawlers.runner import run as scrapy_run

firestore_helper = FirestoreHelper()

def main():
  start_time = time.time()
  
  # Get stores in radius around Orillia
  lat = 44.58857
  lng = -79.415588
  radius = 30
  
  stores = firestore_helper.get_local_stores(lat, lng, radius)
  num_stores = len(stores)
  print(f'\nFound {num_stores} stores within {radius}km of {lat}, {lng}.\n')

  # Shuffle stores so that we don't always start at the same store
  random.shuffle(stores)
  scrapy_run(stores)
  
  print(f'\nAll stores complete. Total time: {time.time() - start_time} seconds.')

  
if __name__ == '__main__':
  main()