import pymongo
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
my_products = client["my_store"]["products"]

bag = {"name": "Gucci", "price": 50000}

print(my_products.insert_one(bag))
