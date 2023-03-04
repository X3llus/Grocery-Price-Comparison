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
    pass

def test_get_closest_store():
    pass

def test_format_loblaws_store_valid():
    # Test valid input
    store = {
        'storeId': '1234',
        'storeBannerId': 'Loblaws',
        'address': {
            'country': 'Canada',
            'line1': '123 Main St',
            'postalCode': 'M1M1M1',
            'town': 'Toronto',
            'region': 'Ontario'
        },
        'geoPoint': {
            'latitude': 43.6532,
            'longitude': -79.3832
        }
    }
    expected_output = {
        'address': {
            'country': 'Canada',
            'formattedAddress': '123 Main St Toronto, Ontario M1M1M1',
            'line1': '123 Main St',
            'postalCode': 'M1M1M1',
            'region': 'Ontario',
            'town': 'Toronto'
        },
        'geoPoint': {
            'latitude': 43.6532,
            'longitude': -79.3832
        },
        'storeId': '1234',
        'type': 'Loblaws'
    }
    assert format_loblaws_store(store) == expected_output

def test_format_loblaws_store_invalid():
    store = {}
    assert format_loblaws_store(store) is None