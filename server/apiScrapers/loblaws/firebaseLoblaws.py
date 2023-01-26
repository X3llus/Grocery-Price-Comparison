import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Going to setup creds with firebase
cred = credentials.Certificate()
firebase_admin.initialize_app(cred)