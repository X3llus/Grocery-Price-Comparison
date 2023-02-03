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
    skusObj = product.get('skus')
    firstSku = skusObj[sku[0]]
    brand = firstSku.get('brand', {}).get('name', "")
    image_url = firstSku.get('images', [{}])[0].get('thumbnail', {}).get('url', "")
  except:
    brand = None
    
  return {
    'productId': id,
    'SKU': sku,
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
      'skuIds': product['SKU']
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
  value = response.get('pricePerUnit', None)
  quantity = response.get('priceCompQty', None)
  unit = response.get('priceCompUomCd', None)
  sku = response.get('offerId', None)
  price = response.get('currentPrice', None)
  
  return {
    'sku': sku,
    'price': price,
    'normalizedPrice': {
      'value': value,
      'quantity': quantity,
      'unit': unit
    }
  }