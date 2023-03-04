import sys
sys.path.insert(0, '../')
# import utils
from utils import distance_between_coords, find_latitude_longitude_range, get_closest_store, format_loblaws_store

# testing how far two different points are from one another
def test_distance_between_coords_km():
    x = distance_between_coords(10,11,12,12,"K")
    # used online calculator to calculate the distance between coordinates kilometers
    assert round(x) == 248 

def test_distance_between_coords_n_mi():
    x = distance_between_coords(10,11,12,12,"N")
    # used online calculator to calculate the distance between coordinates miles
    assert round(x) == 134 

def test_find_latitude_longitude_range():
    # lakehead university coords
    center_lat = 44.608261
    center_lon = -79.437689
    radius_km = 5
    expected_output = {
        "lat_min": 44.56323420905939,
        "lat_max": 44.65328779094061,
        "lon_min": -79.50093555480052,
        "lon_max": -79.37444244519949
    }
    assert find_latitude_longitude_range(center_lat, center_lon, radius_km) == expected_output

def test_get_closest_store_valid():
    user_lat = 44.5920
    user_lng = -79.4586

    stores = [
        {
            'storeId': '0580',
            'storeBannerId': 'zehrs',
            'address': {
                'country': 'Canada',
                'line1': '289 Coldwater Road',
                'postalCode': 'L3V 6J3',
                'town': 'Orillia',
                'region': 'Ontario'
            },
            'geoPoint': {
                'latitude': 44.608261, 
                'longitude': -79.437689
            }
        },
        {
            'storeId': '5678',
            'storeBannerId': 'No Frills',
            'address': {
                'country': 'Canada',
                'line1': '456 Queen St',
                'postalCode': 'M2M 2M2',
                'town': 'Toronto',
                'region': 'Ontario'
            },
            'geoPoint': {
                'latitude': 43.6545,
                'longitude': -79.3793
            }
        }
    ]
    expected_output = {
        'storeId': '0580',
        'storeBannerId': 'zehrs',
        'address': {
            'country': 'Canada',
            'line1': '289 Coldwater Road',
            'postalCode': 'L3V 6J3',
            'town': 'Orillia',
            'region': 'Ontario'
        },
        'geoPoint': {
            'latitude': 44.608261, 
            'longitude': -79.437689
        }
    }
    assert get_closest_store(user_lat, user_lng, stores) == expected_output

def test_format_loblaws_store_valid():
    store = {
        'storeId': '0580',
        'storeBannerId': 'Zehrs',
        'address': {
            'country': 'Canada',
            'line1': '289 Coldwater Road',
            'postalCode': 'L3V 6J3',
            'town': 'Orillia',
            'region': 'Ontario'
        },
        'geoPoint': {
            'latitude': 44.608261, 
            'longitude': -79.437689
        }
    }
    expected_output = {
        'address': {
            'country': 'Canada',
            'formattedAddress': '289 Coldwater Road Orillia, Ontario L3V 6J3',
            'line1': '289 Coldwater Road',
            'postalCode': 'L3V 6J3',
            'region': 'Ontario',
            'town': 'Orillia'
        },
        'geoPoint': {
            'latitude': 44.608261, 
            'longitude': -79.437689
        },
        'storeId': '0580',
        'type': 'Zehrs'
    }
    assert format_loblaws_store(store) == expected_output

def test_format_loblaws_store_invalid():
    store = {}
    assert format_loblaws_store(store) is None