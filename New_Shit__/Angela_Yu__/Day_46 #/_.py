from bs4 import BeautifulSoup
import requests

Url = "https://www.billboard.com/charts/hot-100/"
date = input("Enter a date in Y-M-D:- ") or ""
if date:
    date = date + "/"

Url = Url + date

data = requests.get(url=Url)
data.raise_for_status()
data = data.text
with open("music.html", "w") as file:
    file.write(data)

soup = BeautifulSoup(data, "html.parser")
# print(soup)
