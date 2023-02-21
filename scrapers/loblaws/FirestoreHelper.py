from utils import find_latitude_longitude_range, format_base_product
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirestoreHelper():
  def __init__(self):
    cred = credentials.Certificate('scrapers\serviceAccountKey.json')
    self.app = firebase_admin.initialize_app(cred)
    self.db = firestore.client()
    
    
  def __del__(self):
    firebase_admin.delete_app(self.app)


  def get_local_stores(lat, long, radius):
    db = firestore.client()
    
    range = find_latitude_longitude_range(lat, long, radius)
    
    stores = db.collection(u'Stores')\
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
    

  def save_base_product(self, product, parentCompany):
    base_product = format_base_product(product, parentCompany)
    self.db.collection(u'Products').add(base_product)
    
    
  def process_base_products(self, products, parentCompany):
    num_products = len(products)
    count = 0
    
    for product in products:
      count += 1
      sku = product.get('SKU')
      if sku is None:
        continue
      
      existing = self.get_base_product(sku)
      if existing is None:
        self.save_base_product(product, parentCompany)
      
      if count % 100 == 0:
        print(f'Processed {count} / {num_products} products')