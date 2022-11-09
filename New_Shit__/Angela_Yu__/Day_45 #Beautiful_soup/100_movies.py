from bs4 import BeautifulSoup
import requests
from functools import reduce

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

data = requests.get(url=URL)
data.raise_for_status()
data = data.text
with open("100_html_data.html", "w") as f:
    f.write(reduce(lambda a, b: str(a) + str(b), data))

soup = BeautifulSoup(data, "html.parser")

div = soup.find_all(name="div", class_="jsx-4245974604 listicle-item-content")
with open("100_html_data1.html", "w") as f:
    f.write(reduce(lambda a, b: str(a) + str(b), div))

a = [tag.find_all(name="a", target="_self") for tag in div]

with open("100_html_data2.html", "w") as f:
    f.write(reduce(lambda a, b: str(a) + str(b), a))

print(*a, sep="\n")
