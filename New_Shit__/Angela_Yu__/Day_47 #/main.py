import requests
from json import dump
from bs4 import BeautifulSoup
import time


amazon_url = (
    input("Enter the product url:- ")
    or "https://www.amazon.in/gp/product/B07FTZ259M/ref=ewc_pr_img_1?smid=A3LD4MMBBTHP7M&psc=1"
)
amazon_url = amazon_url.split("product/")[1]
amazon_product_ID = amazon_url.split("/ref")[0]


camel = f"https://camelcamelcamel.com/product/{amazon_product_ID}/"
print(camel)

camel_data = requests.get(url=camel)
camel_data.raise_for_status()
camel_data = camel_data.text

with open("camel.html", "w") as f:
    dump(camel_data, f)

print(camel_data)
