from datetime import datetime
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


def format_base_product(product, store_geo_point):
  return {
    'name': product.get('name', ""),
    'brand': product.get('brand', ""),
    'imageUrl': product.get('imageUrl', ""),
    'size': product.get('packageSize', 1),
    'skus': [product.get('SKU', "")],
    'unit': product.get('normalizedPrice', {}).get('unit', 'ea'),
    '_geoloc': [store_geo_point]
  }


# If the data for the store already exists, updates it. Otherwise, adds it.
def format_product_price(product, store_firestore_id, store_geo_point, store_type):
  return {
    '_geoloc': {
      'latitude': store_geo_point['latitude'],
      'longitude': store_geo_point['longitude']
    },
    'normalized': {
      'quantity': product.get('normalizedPrice', {}).get('quantity', 1),
      'unit': product.get('normalizedPrice', {}).get('unit', 'ea'),
      'value': product.get('normalizedPrice', {}).get('value', 0)
    },
    'price': product.get('price', 0),
    'storeId': store_firestore_id,
    'storeName': store_type,
    'dateExtracted': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
  }
  
def add_store_geo_location(existing_geo_loc_array, store_geo_loc):
  if existing_geo_loc_array is None:
    return [store_geo_loc]
  else:
    for geo_loc in existing_geo_loc_array:
      if geo_loc['latitude'] == store_geo_loc['latitude'] and geo_loc['longitude'] == store_geo_loc['longitude']:
        return existing_geo_loc_array
      
    existing_geo_loc_array.append(store_geo_loc)
    return existing_geo_loc_array