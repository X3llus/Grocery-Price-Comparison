from common import find_latitude_longitude_range, format_base_product, format_product_price, add_store_geo_location
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
      .where(u'skus', u'array_contains', sku)\
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
    

  def add_product_and_store_price(self, store_firestore_id, store_geo_point, store_type, product):
    try:
      product_data = format_base_product(product, store_geo_point)
      price_data = format_product_price(product, store_firestore_id, store_geo_point, store_type)
      product_data['data'] = [price_data]
      
      self.db.collection(u'Products').add(product_data)
    except Exception:
      print(traceback.format_exc())

    
  def save_store(self, store):
    self.db.collection(u'Stores').add(store)
   
  
  # updates or creates store price data for a product
  def handle_store_price(self, product_firestore_id, store_firestore_id, store_geo_point, store_type, product):
    try:
      store_price_dict = format_product_price(product, store_firestore_id, store_geo_point, store_type)
      
      existing_product = self.db.collection('Products')\
        .document(product_firestore_id)\
        .get()\
        .to_dict()
        
      existing_store_price_arr = existing_product.get('data', [])
        
      for i, item in enumerate(existing_store_price_arr):
        if item.get('storeId') == store_firestore_id:
          existing_store_price_arr[i] = store_price_dict
          break
      else:
        existing_store_price_arr.append(store_price_dict)
        
      existing_geo_loc_array = existing_product.get('_geoloc', None)
      updated_geo_loc_array = add_store_geo_location(existing_geo_loc_array, store_geo_point)

      existing_sku_array = existing_product.get('skus', None)
      adding_product_skus = product.get('SKU')

      if adding_product_skus not in existing_sku_array:
        existing_sku_array.append(adding_product_skus)

      self.db.collection('Products')\
        .document(product_firestore_id)\
        .update({
          u'data': existing_store_price_arr,
          u'_geoloc': updated_geo_loc_array,
          u'skus': existing_sku_array
        })
      
    except Exception:
      print(traceback.format_exc())

    
  def delete_store_price(self, productId, storeId):
    product_ref = self.db.collection(u'Products').document(productId)
    store_price_doc = product_ref.collection(u'StorePrices').document(storeId)
    
    if store_price_doc.get().exists:
      store_price_doc.delete()

  def get_pruduct_brand_size(self, brand, size):
      matching_products = self.db.collection(u'Products').where(u'brand', u'==', brand).where(u'size', u'==', size).get()
      if len(list(matching_products)) == 0:
        return None
      else:
        try:
          products = []
          for product in list(matching_products):
            products.append(product.to_dict())
          return products
        except:
          print(traceback.format_exc())
    