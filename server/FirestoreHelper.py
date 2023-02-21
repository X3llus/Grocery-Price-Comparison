from utils import find_latitude_longitude_range, format_walmart_store, format_loblaws_store
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirestoreHelper():
  def __init__(self):
    cred = credentials.Certificate('server\serviceAccountKey.json')
    self.app = firebase_admin.initialize_app(cred)
    self.db = firestore.client()
    
    
  def __del__(self):
    firebase_admin.delete_app(self.app)


  def get_local_stores(self, lat, long, radius):    
    range = find_latitude_longitude_range(lat, long, radius)
    
    stores = self.db.collection(u'Stores')\
    .where(u'geoPoint.longitude', u'>=', range['lon_min'])\
    .where(u'geoPoint.longitude', u'<=', range['lon_max'])\
    .stream()
    
    stores = [store.to_dict() for store in stores]
    stores = [store for store in stores if store['geoPoint']['latitude'] >= range['lat_min'] and store['geoPoint']['latitude'] <= range['lat_max']]
    
    return stores
    

  # hacky way to get stores with the same postal code prefix.
  # query postal code alphabetically
  def get_local_stores_postal(self, postal_code):
    postal_code_prefix = postal_code[:3]
    lastChar = postal_code_prefix[-1]
    i = ord(lastChar) + 1
    next_postal_code_prefix = postal_code_prefix[:-1] + chr(i)
    
    store_query = self.db.collection(u'Stores')\
      .where(u'address.postalCode', u'>=', postal_code)\
      .where(u'address.postalCode', u'<', next_postal_code_prefix)
    
    stores = []
    for store in store_query.stream():
      store_dict = store.to_dict()
      store_dict['id'] = store.reference.id
      stores.append(store_dict)
      
    return stores
  
  def add_loblaws_stores(self, stores):
    print('Number of stores: ', len(stores))
    formatted_stores = [format_loblaws_store(store) for store in stores]
    print('Number of formatted stores: ', len(formatted_stores))
    
    count = 0
    for store in formatted_stores:
      if store is not None:
        self.db.collection(u'Stores').add(store)
        count += 1
        print('Added store: ', count)

  
  def add_walmart_stores(self, stores):
    print('Number of stores: ', len(stores))
    formatted_stores = [format_walmart_store(store) for store in stores]
    print('Number of formatted stores: ', len(formatted_stores))

    count = 0
    for store in formatted_stores:
      if store is not None:
        self.db.collection(u'Stores').add(store)
        count += 1
        print('Added store: ', count)