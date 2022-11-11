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
id_ = "title-of-a-story"
clas = "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"

h3 = soup.find_all(name="h3", id=id_)
print(len(h3))
