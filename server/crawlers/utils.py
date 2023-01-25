from typing import Dict
from crawlers.data import store_locations

def get_store_fsa(storeId, stores):
  fsa = None
  for s in stores:
    if s['id'] == storeId:
      fsa = s['address']['postalCode'][:3]
      break
  
  if fsa is None:
    raise ValueError(f"Store ID {storeId} not found")
  else:
    return fsa


def format_base_product(product: Dict) -> Dict:
  id = product.get('id', "")
  name = product.get('name', "")
  sku = product.get('skuIds', [])
  packageSize = product.get('description', "")
  
  try:
    image_url = product.get('skus', [{}])[0].get('images', [{}])[0].get('thumbnail', {}).get('url', "")
  except:
    image_url = None
  
  try:
    brand = product.get('skus', [{}])[0].get('brand', {}).get('name', "")
  except:
    brand = None
    
  return {
    'productId': id,
    'skuIds': sku,
    'name': name,
    'brand': brand,
    'imageUrl': image_url,
    'packageSize': packageSize
  }
  

def get_price_request_body(products: list[Dict], storeId) -> Dict:
  productIds = []
  for product in products:
    productIds.append({
      'productId': product['productId'],
      'skuIds': product['skuIds']
    })
    
  fsa = get_store_fsa(storeId, store_locations)
    
  return {
    'experience': 'grocery',
    'fsa': fsa,
    'fulfillmentStoreId': str(storeId),
    'lang': 'en',
    'pricingStoreId': str(storeId),
    'products': productIds
  }
  

def trim_price_response(response: Dict) -> Dict:
  value = response['pricePerUnit']
  quantity = response['priceCompQty']
  unit = response['priceCompUomCd']
  
  return {
    'sku': response['offerId'],
    'price': response['currentPrice'],
    'normalizedPrice': {
      'value': value,
      'quantity': quantity,
      'unit': unit
    }
  }