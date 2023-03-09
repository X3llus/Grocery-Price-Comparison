import sys
sys.path.insert(0, '../')
from FirestoreHelper import FirestoreHelper as FH

#from FirestoreHelper import FirestoreHelper as FH

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
    ins = FH()
    expectedValue = [{
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
            'id': 'ZVXbkMJpMR58CmDzx0DU',
            'storeId': '0580',
            'type': 'zehrs'
        }]
    assert ins.get_local_stores_postal('L3V 6J3') == expectedValue

def test_add_loblaws_stores():
    ins = FH()
    loblaws_stores = [
        {'name': 'Loblaws 1', 'address': '123 Main St', 'city': 'Toronto', 'province': 'ON', 'postal_code': 'M1M 1M1'},
        {'name': 'Loblaws 2', 'address': '456 Queen St', 'city': 'Montreal', 'province': 'QC', 'postal_code': 'H1H 1H1'},
    ]
    ins.add_loblaws_stores(loblaws_stores)
    for store in loblaws_stores:
        doc_ref = ins.db.collection('stores').document(store['name'])
        doc = doc_ref.get()
        assert doc.exists
        assert doc.to_dict() == store
    pass

def test_add_walmart_stores():
    pass