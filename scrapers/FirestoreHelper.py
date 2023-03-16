from common import find_latitude_longitude_range, format_base_product, format_product_price
import firebase_admin
import traceback
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
    
    stores_query = self.db.collection(u'Stores')\
    .where(u'geoPoint.longitude', u'>=', range['lon_min'])\
    .where(u'geoPoint.longitude', u'<=', range['lon_max'])
    
    stores = []
    for store in stores_query.stream():
      store_dict = store.to_dict()
      store_dict['id'] = store.reference.id
      stores.append(store_dict)
    
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
      try:        
        product_dict = list(existing)[0].to_dict()
        product_dict['id'] = list(existing)[0].id
        return product_dict
      except Exception:
        print(traceback.format_exc())
        return None
    

  def add_product_and_store_price(self, product, store_id, store_type):
    try:
      product_data = format_base_product(product, store_type)
      price_data = format_product_price(product)
      batch = self.db.batch()
      product_ref = self.db.collection('Products').document()
      batch.set(product_ref, product_data)
      store_price_ref = product_ref.collection('StorePrices').document(store_id)
      batch.set(store_price_ref, price_data)
      batch.commit()
    except Exception:
      print(traceback.format_exc())

    
  def save_store(self, store):
    self.db.collection(u'Stores').add(store)
   
  
  # adds store price to product if product is in stock, else deletes store price
  def handle_store_price(self, product_firestore_id, store_firestore_id, product, inStock=True):
    try:
      store_price_data = format_product_price(product)
      
      product_ref = self.db.collection('Products').document(product_firestore_id)
      store_prices_ref = product_ref.collection('StorePrices')
      
      # # Check if the sub-collection exists, create it if it doesn't
      if not store_prices_ref.get():
        store_prices_ref.document()  # creates an empty document to create the sub-collection
      
      if inStock:
        store_price_doc_ref = store_prices_ref.document(store_firestore_id)
        store_price_doc_ref.set(store_price_data)
      else:
        self.delete_store_price(product_firestore_id, store_firestore_id)
    except Exception:
      print(traceback.format_exc())

    
  def delete_store_price(self, productId, storeId):
    product_ref = self.db.collection(u'Products').document(productId)
    store_price_doc = product_ref.collection(u'StorePrices').document(storeId)
    
    if store_price_doc.get().exists:
      store_price_doc.delete()
    