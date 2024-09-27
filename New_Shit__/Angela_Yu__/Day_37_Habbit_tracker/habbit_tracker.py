import requests
from datetime import datetime

TOKEN = "1_7V'=[&635E=8L@Iy"
USERNAME = "nicozero69"
GRAPH_ID = "python1"

TODAY_DATE = str(datetime(year=2022, month=10, day=20).strftime("%Y%m%d"))
# print(TODAY_DATE)

"https://pixe.la/v1/users/nicozero69/graphs/python1.html"

# 1. creating a new user in pixela

# pixela_endpoint = "https://pixe.la/v1/users"

# parameters = {
# "token": "1_7V'=[&635E=8L@Iy",
# "username": "nicozero69",
# "agreeTermsOfService": "yes",
# "notMinor": "yes",
# }

# post_data = requests.post(url=pixela_endpoint, json=parameters)

# print(post_data.text)


# 2. creating a graph in pixela

# pixela_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

# pixela_header = {"X-USER-TOKEN": TOKEN}

# parameters = {
# "id": "python1",
# "name": "Python",
# "unit": "min",
# "type": "int",
# "color": "ajisai",
# }

# post_data = requests.post(
# url=pixela_graph_endpoint, headers=pixela_header, json=parameters
# )

# print(post_data.text)


# 3. Posting a pixel in pixela graph

# pixela_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

# pixela_header = {"X-USER-TOKEN": TOKEN}

# parameters = {
# "date": TODAY_DATE,
# "quantity": "3",
# "optionalData": "",
# }

# post_data = requests.post(
# url=pixela_graph_endpoint, headers=pixela_header, json=parameters
# )

# print(post_data.text)

# 4. PUT request

# pixela_graph_endpoint = (
#     f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{TODAY_DATE}"
# )

# pixela_header = {"X-USER-TOKEN": TOKEN}

# parameters = {
#     "quantity": "5000",
# }

# post_data = requests.put(
#     url=pixela_graph_endpoint, headers=pixela_header, json=parameters
# )

# print(post_data.text)


# 4. DELETE request to delete pixela graph data

# pixela_graph_endpoint = (
#     f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{TODAY_DATE}"
# )

# pixela_header = {"X-USER-TOKEN": TOKEN}

# post_data = requests.delete(url=pixela_graph_endpoint, headers=pixela_header)

# print(post_data.text)
