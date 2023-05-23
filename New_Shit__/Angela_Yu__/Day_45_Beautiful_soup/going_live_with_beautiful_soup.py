from bs4 import BeautifulSoup
import requests


def show_all_news():
    for i, j in zip(upvote, news):
        print(j, ":- ", i)


def highest_upvote():
    h_up = max(upvote)
    h_up_index = upvote.index(h_up)
    print(news[h_up_index], ":- ", h_up, "\nThe URL :- ", url[h_up_index])


web_site_url = "https://news.ycombinator.com/news"

web_site_data = requests.get(web_site_url)
web_site_data.raise_for_status()
web_site_data = web_site_data.text

with open("web_site.html", "w") as f:
    f.write(web_site_data)

soup = BeautifulSoup(web_site_data, "html.parser")

all_a = [tag.select_one("a") for tag in soup.find_all(name="span", class_="titleline")]
all_span = soup.find_all(name="span", class_="score")
news = [tag.getText() for tag in all_a]
url = [tag.get("href") for tag in all_a]
upvote = [int(number.split(" ")[0]) for number in [tag.getText() for tag in all_span]]

highest_upvote()
show_all_news()