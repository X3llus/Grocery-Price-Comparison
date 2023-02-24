import traceback
from dotenv import dotenv_values
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from common import format_product_price

class RealtimeDbHelper():
  def __init__(self):
    config = dotenv_values('C:\Lakehead\Winter2023\COMP4431-AdvancedProject\Grocery-Price-Comparison\scrapers\.env')
    db_url = config.get('FIREBASE_DB_URL')
    uid = config.get('FIREBASE_UID')
    cred = credentials.Certificate('serviceAccountKey.json')
    
    try:
      self.app = firebase_admin.get_app('realtime-db')
    except ValueError:    
      self.app = firebase_admin.initialize_app(cred, {
        'databaseURL': db_url,
        'databaseAuthVariableOverride': {
          'uid': uid
        }
      }, name='realtime-db')
      
      
  def __del__(self):
    try:
      realtime_app = firebase_admin.get_app('realtime-db')
      firebase_admin.delete_app(realtime_app)
    except ValueError:
      pass
    
    
  def get_product_price(self, sku, store_type, store_id):
    try:
      ref = db.reference(f'store-prices/{store_type}-{store_id}-{sku}')
      return ref.get()
    except:
      print(traceback.format_exc())
      return None
    
    
  def save_product_price(self, store_type, store_id, product):
    sku = product.pop('SKU')
    product_price = format_product_price(product)
    
    try:
      ref = db.reference('store-prices')
      ref.child(f'{store_type}-{store_id}-{sku}').set(product_price)
    except:
      print(f'Error saving product price {sku} for store {store_type}-{store_id}')
      print(traceback.format_exc())