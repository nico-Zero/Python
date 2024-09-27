from itertools import count
import logging
import json
from textwrap import indent
person = {"name":"jhon","age":30,"city":"New York","hasChildren":False,"titles":["engineer","programmer"]}
# logging.error(person)

# personJSON = json.dumps(person, indent =4 ,sort_keys = True)

# # print(personJSON)
# # print(person)

# # with open("person.json", "w") as file:
# #     json.dump(person,file,indent=4)
# with open("/media/zero/Software/__/Python/Intermediate/person.json","r") as file:
#     person = json.load(file)
#     print(person)

class User:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o , User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")

for i in count(0):
    namex = input("Enter user name : ")
    agex = input("Enter user age : ")
    print()

    user = User(str(namex), int(agex))

    with open("/media/zero/Software/__/Python/Intermediate/person.json", "w") as file:
        json.dump(user,file,indent=4, default= encode_user)
    # userJSON = json.dumps(user, default= encode_user)
    # print(userJSON)

userJSON = json.dumps(user, default= encode_user)   
def decode (dict):
    if User.__name__ in dict:
        return User(name= dict["name"], age = dict["age"])
    return dict

user = json.loads(userJSON , object_hook = decode)
print(user.age)
