import pymongo
from pymongo import MongoClient
from faker import Faker
from random import randint

f_data = Faker()

client = MongoClient("mongodb://localhost:27017")
my_emp = client["my_store"]["emp"]
# my_emp.delete_many({})

# [print(i) for i in my_emp.find({"age": 29})]

# cursor = my_emp.find()
# print(cursor.alive)

# for i in cursor:
#     print(i)

# print(cursor.alive)

## sort()

# for i in my_emp.find({}).sort(
#     [("age", pymongo.ASCENDING), ("name", pymongo.ASCENDING)]
# ):
#     print(i)

# for i in my_emp.find({}).limit(5):
#     print(i)

# page_limit = 5

# for i in range(0, 4):
#     print(f"\n--Page {i+1}--")
#     for i in (
#         my_emp.find({})
#         .sort([("age", pymongo.ASCENDING), ("name", pymongo.ASCENDING)])
#         .skip(i * page_limit)
#         .limit(page_limit)
#     ):
#         print(i)

# skip = my_emp.find({}).skip(5)

# print(skip.count(with_limit_and_skip=True))

# print(my_emp.distinct("age"))


# -------------------------------------------- Projection-------------------------------------
find = my_emp.find(
    {},
    {
        "_id": 0,
        "name": 1,
    },
)

for i in find:
    print(i)
