import requests

URL = "https://www.google.co.in/"

data = requests.get(url=URL)
data.raise_for_status()
data = data.text

with open("data.html","w") as file:
    file.write(data)

print(data)
