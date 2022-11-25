import pymongo
from pymongo import MongoClient
from faker import Faker

f_data = Faker()

client = MongoClient("mongodb://localhost:27017")
my_products = client["my_store"]["products"]

# bag = [
#     {"name": f_data.factories(), "price": f_data.random_number()}
#     for _ in range(int(input("Enter the number of entries:- ")))
# ]

# print(my_products.insert_many(bag))

# my_products.delete_many({})

print(f_data.job())
