from FirestoreHelper import FirestoreHelper
from data import walmart_stores, loblaws_stores


db = FirestoreHelper()

#db.add_walmart_stores(walmart_stores)
db.add_loblaws_stores(loblaws_stores)