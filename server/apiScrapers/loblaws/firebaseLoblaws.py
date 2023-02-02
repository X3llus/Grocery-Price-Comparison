import asyncio
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from loblawsScraper import get_all_products
from data import categories

# from loblawsScraper import 
category = ["preparedMeals","meat","fishAndSeafood","fruitsAndVegetables","deli","bakery","dairyAndEggs","drinks","frozen","pantry","naturalFoods","beerAndWine","snacksChipsAndCandy","internationalFoods"]
# Going to setup creds with firebase
cred = credentials.Certificate("server\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

products = asyncio.run(get_all_products())

# word_list = [key for key in category.keys()]
print(products.items())
# print(word_list)
# print(word_list[0])
# print(word_list[1])
# db.collection().add({}) mock code for adding documents to the database

for i in range(0, len(category)):
    for u in range(0, len(products[category[i]])):
        data={
            "name": [products[category[i]][u]["name"]],
            "brand": [products[category[i]][u]["brand"]],
            "imageUrl": [products[category[i]][u]["imageUrl"]],
            "packageSize": [products[category[i]][u]["packageSize"]]
        }
        db.collection("Products").add(
            data)
        # print(products[category[i]][u]["name"])
        # print(products[category[i]][u]["brand"])
        # print(products[category[i]][u]["imageUrl"])
        # print(products[category[i]][u]["packageSize"])
        

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
# print(products.items())