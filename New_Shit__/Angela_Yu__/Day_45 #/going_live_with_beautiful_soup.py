from bs4 import BeautifulSoup
import requests

web_site_url = "https://news.ycombinator.com/news"

web_site_data = requests.get(web_site_url)
web_site_data.raise_for_status()
web_site_data = web_site_data.text

with open("web_site.html", "w") as f:
    f.write(web_site_data)

soup = BeautifulSoup(web_site_data, "html.parser")

all_span = soup.find_all(name="span", class_="titleline")
all_a = [tag.select_one("a") for tag in all_span]
string = [tag.string for tag in all_a]
href = [tag.get("href") for tag in all_a]

print(len(string))
# print(*string, sep="\n")

all_span = soup.find_all(name="span", class_="score")
scores = [tag.string for tag in all_span]

print(len(scores))
# print(*scores, sep="\n")

