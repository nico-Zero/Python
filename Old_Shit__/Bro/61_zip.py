username = ["Dude","Bro","Mister"]
password = ["p@ssword","abc123","guest"]
last_login = ["1/1/2201","12/4/9023","9,23,8934"]

user = list(zip(username,password,last_login))

# print(user)
print(type(user))

for i,j,o in user:
    print(f"username: {i}, password: {j}, last-login: {o}")
    
