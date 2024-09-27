import requests
from json import dump
from bs4 import BeautifulSoup
import time


amazon_url = (
    input("Enter the product url:- ")
    or "https://www.amazon.in/gp/product/B07FTZ259M/ref=ewc_pr_img_1?smid=A3LD4MMBBTHP7M&psc=1"
)

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept-Language": "en-US,en;q=0.5",
}

PRICE = int(input("Check if the price is or lower then:- "))
product_data = requests.get(url=amazon_url, headers=header)
product_data.raise_for_status()
product_data = product_data.text

with open("product_data.html", "w") as f:
    dump(product_data, f)

parsed_amazon_data = BeautifulSoup(product_data, "html.parser")
span_class_name = "a-price-whole"
data = parsed_amazon_data.find(name="span", class_=span_class_name)

price = int(data.getText()[:-1].replace(",", ""))

if price < PRICE:
    print("Yoo we got a good deal...")
    print(price)
else:
    print("Sorry, man no deal right now!!!")
