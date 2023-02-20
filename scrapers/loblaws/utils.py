import math
from typing import Dict, List
from datetime import datetime

def distance_between_coords(lat1, lon1, lat2, lon2, unit):
  radlat1 = math.pi * lat1/180
  radlat2 = math.pi * lat2/180
  theta = lon1-lon2
  radtheta = math.pi * theta/180
  dist = math.sin(radlat1) * math.sin(radlat2) + math.cos(radlat1) * math.cos(radlat2) * math.cos(radtheta)
  
  if dist > 1:
    dist = 1
  
  dist = math.acos(dist)
  dist = dist * 180/math.pi
  dist = dist * 60 * 1.1515
  
  if unit == "K":
    dist = dist * 1.609344
  elif unit == "N":
    dist = dist * 0.8684
    
  return dist

def find_latitude_longitude_range(center_lat, center_lon, radius_km):
    d_lat = radius_km / 111.045
    latitude_min = center_lat - d_lat
    latitude_max = center_lat + d_lat
    
    d_lon = radius_km / (111.045 * math.cos(center_lat * (math.pi/180)))
    longitude_min = center_lon - d_lon
    longitude_max = center_lon + d_lon
    
    return  {
      "lat_min": latitude_min,
      "lat_max": latitude_max,
      "lon_min": longitude_min,
      "lon_max": longitude_max
    }
  
def get_closest_store(user_lat, user_lng, stores):
  closest_store = None
  closest_distance = float('inf')

  for store in stores:
    distance = distance_between_coords(user_lat, user_lng, store['geoPoint']['latitude'], store['geoPoint']['longitude'], "K")
    if distance < closest_distance:
      closest_distance = distance
      closest_store = store

  if 'storeBannerId' in closest_store and 'name' in closest_store:
    print(f"Closest store is a {closest_store['storeBannerId']} in {closest_store['name']} at {closest_distance}km away")
  else:
    print(f"Closest store is {closest_distance}km away")

  return closest_store

def format_product(product: Dict) -> Dict:
  
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
    'dateExtracted': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
  }


def format_product_price(product: Dict) -> Dict:
  return {
    'inStock': product.get('inStock', False),
    'price': product.get('price', 0),
    'normalizedPrice': product.get('normalizedPrice', {}),
    'dateExtracted': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
  }
  
  
def format_base_product(product: Dict) -> Dict:
  return {
    'name': product.get('name', ""),
    'brand': product.get('brand', ""),
    'imageUrl': product.get('imageUrl', ""),
    'packageSize': product.get('packageSize', "")
  }

  
def filter_unique_products(all_products: List) -> List:
  return list({product['SKU']: product for product in all_products}.values())