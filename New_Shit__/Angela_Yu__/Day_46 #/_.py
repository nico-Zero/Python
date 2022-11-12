# from bs4 import BeautifulSoup
# import requests
# from functools import reduce


# Url = "https://www.billboard.com/charts/hot-100/"
# date = input("Enter a date in Y-M-D:- ") or ""
# if date:
#     date = date + "/"

# Url = Url + date

# data = requests.get(url=Url)
# data.raise_for_status()
# data = data.text

# soup = BeautifulSoup(data, "html.parser")
# clas = "lrv-u-width-100p"

# li = soup.find_all(name="li", class_=clas)


# with open("music.html", "w") as file:
#     file.write(reduce(lambda x, y: str(x) + str(y), li))

# h3 = [
#     tag.select(selector="ul li h3")[0]
#     for tag in li
#     if len(tag.select(selector="ul li h3")) != 0
# ]

# unfiltered_song_names = [tag.getText().removeprefix() for tag in h3]


# print(*unfiltered_song_names, sep="\n")

x = "     sdf io      "
new_x = ""
j = 0


for i in x:
    if i == " " and j == 0:
        continue
    else:
        new_x = new_x + i
        j += 1

print("==" + new_x + "==")
