import traceback
from dotenv import dotenv_values
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from utils import format_base_product, format_product_price

class RealtimeDbHelper():
  def __init__(self):
    config = dotenv_values('C:\Lakehead\Winter2023\COMP4431-AdvancedProject\Grocery-Price-Comparison\scrapers\.env')
    db_url = config.get('FIREBASE_DB_URL')
    uid = config.get('FIREBASE_UID')
    cred = credentials.Certificate('scrapers\serviceAccountKey.json')
    self.app = firebase_admin.initialize_app(cred, {
      'databaseURL': db_url,
      'databaseAuthVariableOverride': {
        'uid': uid
      }
    })
    
    
  def __del__(self):
    firebase_admin.delete_app(self.app)
    
    
  def get_base_product(self, sku):
    try:
      ref = db.reference(f'products/{sku}')
      return ref.get()
    except:
      return None


  def get_product_price(self, sku, store_type, store_id):
    try:
      ref = db.reference(f'store-prices/{store_type}-{store_id}-{sku}')
      return ref.get()
    except:
      print(traceback.format_exc())
      return None


  def save_base_product(self, base_product, sku):
    try:
      ref = db.reference('products')
      ref.child(sku).set(base_product)
    except:
      print(f'Error saving base product {sku}')
      print(traceback.format_exc())
      return None
    
    
  def save_product_price(self, store_type, store_id, sku, product_price):
    try:
      ref = db.reference('store-prices')
      ref.child(f'{store_type}-{store_id}-{sku}').set(product_price)
    except:
      print(f'Error saving product price {sku} for store {store_type}-{store_id}')
      print(traceback.format_exc())
    
    
  def process_products(self, store_type, store_id, products):
    num_products = len(products)
    count = 0
    reads = 0
    writes = 0
    
    for product in products:
      sku = product.pop('SKU')
      existing = self.get_base_product(sku)
      reads += 1
      if existing is None:
        base_product = format_base_product(product)
        self.save_base_product(base_product, sku)
        writes += 1

      product_price = format_product_price(product)
      self.save_product_price(store_type, store_id, sku, product_price)
      writes += 1
      count += 1
      print(f'Processed {count} / {num_products} products')
      
    print('Done processing products')
    print(f'Number of reads: {reads}')
    print(f'Number of writes: {writes}')
      