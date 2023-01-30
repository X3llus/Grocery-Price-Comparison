import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from data import store_locations

# Going to setup creds with firebase
cred = credentials.Certificate("server\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# iterates through the store locations from data.py which populates Stores collectoin in firebase
for dataset in store_locations:
    db.collection("Stores").add(dataset)