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


  def get_product_price(self, sku, store_type, store_id):
    try:
      ref = db.reference(f'store-prices/{store_type}-{store_id}-{sku}')
      return ref.get()
    except:
      print(traceback.format_exc())
      return None
    
    
  def save_product_price(self, store_type, store_id, sku, product_price):
    try:
      ref = db.reference('store-prices')
      ref.child(f'{store_type}-{store_id}-{sku}').set(product_price)
    except:
      print(f'Error saving product price {sku} for store {store_type}-{store_id}')
      print(traceback.format_exc())
    
    
  def process_product_prices(self, store_type, store_id, products):
    num_products = len(products)
    
    for product in products:
      count += 1
      sku = product.pop('SKU')
      
      product_price = format_product_price(product)
      self.save_product_price(store_type, store_id, sku, product_price)
      
      if count % 100 == 0:
        print(f'Processed {count} / {num_products} products')
      