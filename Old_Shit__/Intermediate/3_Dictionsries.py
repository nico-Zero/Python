dic = {"name": "Max", "age": 28, "city": "New York"}
print(dic)

dic2 = dict(name="Mary", age=28, city="Boston")
print(dic2)

dic["email"] = "nico_zero_0.gmail.com"
value = dic["email"]
print(value)

dic["email"] = "ZEROXXXX .gmail.com"
value = dic["email"]
print(value)

del dic["name"]
print(dic)

dic.pop("age")
print(dic)

dic.popitem()
print(dic)

if "city" in dic:
    print(dic["city"])

try:
    print(dic["name"])
except:
    print("Could not find")

for key in dic.keys():
    print(key)

print(dic)

for key, values in dic.items():
    print(key, values, sep=": ")

dic_cpy = dic.copy()

print(dic_cpy)

dic_cpy1 = dict(dic)

print(dic_cpy1)


dic_x = {"name": "Max", "age": 28, "city": "New York"}
dic_z = dict(name="Zanos", age=69, city="Sostanls")

dic_x.update(dic_z)

print(dic_x)
