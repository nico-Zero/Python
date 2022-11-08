from bs4 import BeautifulSoup

# import lxml -> If the html.parser does not work ro give an error about the parser.


with open("example/index.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
print(soup.a)
print(soup.a.string)
