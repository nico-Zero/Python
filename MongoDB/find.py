import pymongo
from pymongo import MongoClient
from faker import Faker
from random import randint

f_data = Faker()

client = MongoClient("mongodb://localhost:27017")
my_emp = client["my_store"]["emp"]
# my_emp.delete_many({})

# [print(i) for i in my_emp.find({"age": 29})]

cursor = my_emp.find()
print(cursor.alive)

for i in cursor:
    print(i)

print(cursor.alive)

# sort()

for i in cursor.sort("price", pymongo.ASCENDING):
    print(i)
