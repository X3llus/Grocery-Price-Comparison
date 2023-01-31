import asyncio
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from loblawsScraper import get_all_products
from data import categories

# from loblawsScraper import 
# category = ["preparedMeals"]["meat"]["fishAndSeafood"]["fruitsAndVegetables"]["deli"]["bakery"]["dairyAndEggs"]["drinks"]["frozen"]["pantry"]["naturalFoods"]["beerAndWine"]["snacksChipsAndCandy"]["internationalFoods"]
# Going to setup creds with firebase
cred = credentials.Certificate("server\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

products = asyncio.run(get_all_products())

# db.collection().add({}) mock code for adding documents to the database
for u in range(0, len(products["fishAndSeafood"])):
    print(products["fishAndSeafood"][u]["name"])
    # head, sep, tail = categories[u].partition(':')
    # print(head)
    # for i in range(0, len(products[head])):
    #     print(products[head][i]["name"])
# print(type(products))
# productsValue = list(products.values())
# print(type(productsValue))
# print(productsValue[1])
# print(productsValue[1]["Name"])
# db.collection('products').add({
# products
# })
