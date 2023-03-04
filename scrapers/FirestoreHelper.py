from common import find_latitude_longitude_range, format_base_product
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirestoreHelper():
  def __init__(self):
    cred = credentials.Certificate('serviceAccountKey.json')
    try:
      self.app = firebase_admin.get_app('firestore')
    except ValueError:
      self.app = firebase_admin.initialize_app(cred, name='firestore')
    self.db = firestore.client(self.app)
      

  def __del__(self):
    try:
      firebase_app = firebase_admin.get_app('firestore')
      firebase_admin.delete_app(firebase_app)
    except ValueError:
      pass


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
  # query postal code alphabetically to be able to get all stores with the same prefix
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


  def get_base_product(self, sku):
    existing = self.db.collection(u'Products')\
      .where(u'SKU', u'==', sku)\
      .get()
      
    if len(list(existing)) == 0:
      return None
    else:
      return list(existing)[0].to_dict()
    

  def save_base_product(self, product, store_type):
    base_product = format_base_product(product, store_type)
    self.db.collection(u'Products').add(base_product)
    
    
  def save_store(self, store):
    self.db.collection(u'Stores').add(store)