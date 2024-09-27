# import requests
# import time
#
# base_url = "https://apipanel.aepsapp.in"
# token = "alsdjfklasdlkjflakjsdjfllaskldjlkfjasdj"
# endpoint = "/api/payout/do-payout"
#
# header = {
#         'Authorization': "Bearer " + token,
# }
#
# def send_request():
#     response = requests.get(base_url + endpoint, headers=header)
#     print(response.status_code, response.text)
#
# requests_per_minute = 20
# interval = 60 / requests_per_minute
#
# for _ in range(requests_per_minute):
#     send_request()
#     time.sleep(interval)
#


# i = 1
# while i:
#     print("Hello, World!")
# else:
#     print("Error")

# num = 10
# for i in range(1, num + 1):
#     if i == 3:
#         break
#     else:
#         print("Hello, World! ", i)


# def __print_num(string):
#     total = []
#     for c in string:
#         print(c, "=", ord(c), sep=" ")
#         total.append(ord(c))
#     print("Total:- ", sum(total))
#
#
# def print_all(names):
#     for name in names:
#         __print_num(name)
#
#
# names = ["dat", "dog"]
# print_all(names)
# print(f"{names[0]} < {names[1]} :-", names[0] < names[1])


# n = (4, 2**3, 23, 18, 19)
# print(n[1])
n_dir = {
    "name": "yvuraj mahilange",
    "age": 21,
    "city": "Korba",
}

print(n_dir["name"])
print(n_dir["age"])
print(n_dir["city"])
