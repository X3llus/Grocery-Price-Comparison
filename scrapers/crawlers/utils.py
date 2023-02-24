from typing import Dict
from crawlers.data import store_locations

def get_store_fsa(storeId, stores):
  fsa = None
  for s in stores:
    if str(s['id']) == storeId:
      fsa = s['address']['postalCode'][:3]
      break
  
  if fsa is None:
    raise ValueError(f"Store ID {storeId} not found")
  else:
    return fsa


def format_product(product: Dict) -> Dict:
  try:
    id = product.get('id')
    name = product.get('name')
    sku = product.get('skuIds')
    packageSize = product.get('description')
    skusObj = product.get('skus')
    firstSku = skusObj[sku[0]]
    brand = firstSku.get('brand', {}).get('name', "")
    image_url = firstSku.get('images', [{}])[0].get('thumbnail', {}).get('url', "")
  except:
    return None
    
  return {
    'productId': id,
    'SKU': sku,
    'name': name,
    'brand': brand,
    'imageUrl': image_url,
    'packageSize': packageSize,
  }
  
  
def format_loblaws_product(product: Dict) -> Dict:
  try:
    sku = product.get('code')
  except:
    return None
  
  try:
    price = product.get('prices', {}).get('price', {}).get('value', 0)
  except:
    price = 0
    
  try:
    image_url = product.get('imageAssets', [{}])[0].get('mediumUrl', "")
  except:
    image_url = None
    
  try:
    in_stock = product.get('stockStatus', "")
    in_stock = in_stock == "OK"
  except:
    in_stock = False
    
  try:
    size_unit = product.get('prices', {}).get('comparisonPrices', [{}])[0].get('unit', "ea")
    normalized = product.get('prices', {}).get('comparisonPrices', [{}])[0].get('value', 0)
    quantity = product.get('prices', {}).get('comparisonPrices', [{}])[0].get('quantity', 1)
  except:
    size_unit = "ea"
    normalized = price
    quantity = 1
    
  return {
    'name': product.get('name', ""),
    'brand': product.get('brand', ""),
    'imageUrl': image_url,
    'packageSize': product.get('packageSize', ""),
    'inStock': in_stock,
    'price': price,
    'normalizedPrice': {
        'value': normalized,
        'quantity': quantity,
        'unit': size_unit
    },
    'SKU': sku,
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