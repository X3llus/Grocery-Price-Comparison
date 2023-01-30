import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from data import store_locations

# Going to setup creds with firebase
cred = credentials.Certificate("server\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# db.collection().add({}) mock code for adding documents to the database
# def store_data(collection_id, data):
#     db.collection(collection_id).add(data)

# store_data(collection_id = "Stores", data = store_locations)
# print(store_locations)


# print(store_locations[1])
for dataset in store_locations:
    db.collection("Stores").add(dataset)