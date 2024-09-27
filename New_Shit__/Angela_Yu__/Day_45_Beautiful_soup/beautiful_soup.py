from bs4 import BeautifulSoup
import lxml
# import bs4

# import lxml -> If the html.parser does not work ro give an error about the parser.
# and just lxml in place fo html.parser in line 11.

with open("example/index.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)
# print(soup.a)

# all_a = soup.find_all(name="a")
# print(all_a)
# for tag in all_a:
#     print(tag.getText(), ":- ", tag.get("href"))

url = soup.select_one(selector="table p a")
eval("print(url.name)")
