from bs4 import BeautifulSoup
import requests
from functools import reduce


Url = "https://www.billboard.com/charts/hot-100/"
date = input("Enter a date in Y-M-D:- ") or ""
if date:
    date = date + "/"

Url = Url + date

data = requests.get(url=Url)
data.raise_for_status()
data = data.text

soup = BeautifulSoup(data, "html.parser")
clas = "lrv-u-width-100p"

li = soup.find_all(name="li", class_=clas)


with open("music.html", "w") as file:
    file.write(reduce(lambda x, y: str(x) + str(y), li))

song_names = [
    tag.select(selector="ul li h3")
    for tag in li
    if len(tag.select(selector="ul li h3")) != 0
]

print(len(song_names))
print(song_names)
