from bs4 import BeautifulSoup
import requests

web_site_url = "https://news.ycombinator.com/news"

web_site_data = requests.get(web_site_url)
web_site_data.raise_for_status()
web_site_data = web_site_data.text

with open("web_site.html", "w") as f:
    f.write(web_site_data)

soup = BeautifulSoup(web_site_data, "html.parser")

all_tr = soup.find_all(name="tr", class_="athing")
all_span = [tag.find(name="span", class_="titleline") for tag in all_tr]
all_a = [tag.select_one("a") for tag in all_span]


print(len(all_a))
print(*all_a, sep="\n")
