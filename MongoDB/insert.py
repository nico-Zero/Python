import pymongo
from pymongo import MongoClient
from faker import Faker
from random import randint

f_data = Faker()

client = MongoClient("mongodb://localhost:27017")
my_products = client["my_store"]["emp"]
# my_products.delete_many({})

bag = [
    {
        "name": f_data.name(),
        "job": f_data.job(),
        "age": randint(18, 120),
        "phone_no": f_data.phone_number(),
    }
    for _ in range(int(input("Enter the number of entries:- ")))
]

print(my_products.insert_many(bag))
