import time
from FirestoreHelper import FirestoreHelper
from crawlers.runner import run as scrapy_run

firestore_helper = FirestoreHelper()

def main():
  start_time = time.time()
  
  # Get stores in radius around Orillia
  lat = 44.58857
  lng = -79.415588
  radius = 10
  
  stores = firestore_helper.get_local_stores(lat, lng, radius)
  num_stores = len(stores)
  print(f'\nFound {num_stores} stores within {radius}km of {lat}, {lng}.\n')
  print(stores[0])

  # Move Orillia Zehrs to the front of the list
  index_to_move = next((i for i, x in enumerate(stores) if x['type'] == 'Metro'), None)
  if index_to_move is not None:
    moved_dict = stores.pop(index_to_move)
    stores.insert(0, moved_dict)
    
  scrapy_run(stores)
  
  print(f'\nAll stores complete. Total time: {time.time() - start_time} seconds.')

  
if __name__ == '__main__':
  main()