from pymongo import MongoClient

# my_client = MongoClient("localhost",27017)
my_client = MongoClient("mongodb://localhost:27017")
print(my_client, "\n")

# databases = my_client.list_database_names()
# print(databases)

# my_store_db = my_client.my_store
my_store_db = my_client["my_store"]
print(my_store_db)
print(my_store_db.list_collection_names())

user_db_collection = my_store_db.users
# # CRUD
# # C = Create
# print(user_db_collection.insert_one({"name": "Filcon", "age": "Hunting"}))


# # R = Read
# print(user_db_collection.find_one({"name": "zero"}))

# # U = Update
# print(
#     user_db_collection.update_one(
#         {"name": "zero"}, {"$set": {"name": "nova", "job": "Groom"}}
#     )
# )

# # D = Delete
# print(user_db_collection.delete_one({"name": "Filcon"}))
