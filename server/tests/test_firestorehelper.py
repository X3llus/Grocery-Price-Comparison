import sys
sys.path.insert(0, '../')
from FirestoreHelper import FirestoreHelper as FH

def test_get_local_stores():
    ins = FH()
    expectedValue = [
        {
            'address': {
                'town': 'Orillia', 
                'region': 'ON', 
                'line1': '175 Murphy Rd', 
                'formattedAddress': '175 Murphy Rd Orillia, ON L3V 0B5', 
                'postalCode': 'L3V 0B5', 
                'country': 'CA'
            }, 
            'geoPoint': {
                'latitude': 44.61571, 
                'longitude': -79.445723
            }, 
            'storeId': '3153', 
            'type': 'Walmart'
        }, 
        {
            'address': {
                'town': 'Orillia', 
                'region': 'Ontario', 
                'line1': '289 Coldwater Road', 
                'formattedAddress': '289 Coldwater Road Orillia, Ontario L3V 6J3', 'postalCode': 'L3V 6J3', 
                'country': 'Canada'
            },
            'geoPoint': {
                'latitude': 44.608261, 
                'longitude': -79.437689
            },
            'storeId': '0580',
            'type': 'zehrs'
        }]
    assert ins.get_local_stores(44.608261,-79.437689,1) == expectedValue

def test_get_local_stores_postal():
    pass

def test_add_loblaws_stores():
    pass

def test_add_walmart_stores():
    pass