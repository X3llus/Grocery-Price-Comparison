import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from loblawsScraper import get_all_products, get_products

# Going to setup creds with firebase
cred = credentials.Certificate("server\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# db.collection().add({}) mock code for adding documents to the database
# def store_data(collection_id, data):
#     db.collection(collection_id).add(data)

# store_data(collection_id = "Store", data = data.store_locations)