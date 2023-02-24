import datetime
import math

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


def format_base_product(product, store_type):
  return {
    'name': product.get('name', ""),
    'brand': product.get('brand', ""),
    'imageUrl': product.get('imageUrl', ""),
    'packageSize': product.get('packageSize', ""),
    'SKU': product.get('SKU', ""),
    'parentCompany': store_type,
    'dateExtracted': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
  }


def format_product_price(product):
  return {
    'inStock': product.get('inStock', False),
    'price': product.get('price', 0),
    'normalizedPrice': product.get('normalizedPrice', {}),
    'dateExtracted': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
  }