from bs4 import BeautifulSoup
import requests
from functools import reduce


def remove_space(string):
    for i in string:
        if i == " " or i == "\n" or i == "\t":
            string = string[1:]
        else:
            break
    for i in string[::-1]:
        if i == " " or i == "\n" or i == "\t":
            string = string[:-1]
        else:
            break
    return string


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

h3 = [
    tag.select(selector="ul li h3")[0]
    for tag in li
    if len(tag.select(selector="ul li h3")) != 0
]

unfiltered_song_names = [tag.getText() for tag in h3]
filtered_song_names = [remove_space(i) for i in unfiltered_song_names]
song_names = [
    str(position) + ". " + i for position, i in enumerate(filtered_song_names, start=1)
]


print(*song_names, sep="\n")
