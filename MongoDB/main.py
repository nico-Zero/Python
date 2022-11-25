from pymongo import MongoClient

# my_client = MongoClient("localhost",27017)
my_client = MongoClient("mongodb://localhost:27017")
print(my_client,"\n")

# databases = my_client.list_database_names()
# print(databases)

# my_store_db = my_client.my_store
my_store_db = my_client["my_store"]

print(my_store_db)
