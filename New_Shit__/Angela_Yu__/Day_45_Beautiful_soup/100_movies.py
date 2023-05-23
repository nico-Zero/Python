from bs4 import BeautifulSoup
import requests
from functools import reduce

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

data = requests.get(url=URL)
data.raise_for_status()
data = data.text

soup = BeautifulSoup(data, "html.parser")
div = soup.find_all(name="div", class_="jsx-4245974604 listicle-item-content")
with open("100_html_data1.html", "w") as f:
    f.write(reduce(lambda a, b: str(a) + str(b), div))


a = [tag.find_all(name="a") for tag in div]
all_a_string = []
for i in a:
    [all_a_string.append(x.getText()) for x in i]

movie_names = [
    i.split("review of ")[1] for i in all_a_string if i.count("Read Empire's review of")
]

list_of_movies = [
    str(i[0]) + ". " + i[1] for i in enumerate(reversed(movie_names), start=1)
]
with open("100_movies_list.txt", "w") as file:
    file.write(reduce(lambda x, y: x + "\n" + y, list_of_movies))

print(*list_of_movies, sep="\n")
