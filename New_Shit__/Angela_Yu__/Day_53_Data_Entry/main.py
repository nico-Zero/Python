from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests
from time import sleep
from os import system


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

form_link = "https://docs.google.com/forms/d/e/1FAIpQLScJXp_yzZ6mOH7QtZUdub0mMvfyXyfdDCvtn4wZPEbF-hawqw/viewform?usp=sf_link"

with open("index.html", "r") as index_html:
    data = index_html.read()

soup = BeautifulSoup(data, "html.parser")
data_list = soup.find_all(
    name="li",
    class_="ListItem-c11n-8-84-0__sc-10e22w8-0 StyledListCardWrapper-srp__sc-wtsrtn-0 cTMokP gTOWtl",
)

print(f"Total Property Found:- {len(data_list)}")
property_detail = []

for fragment_list in data_list:
    address = fragment_list.select_one(selector="div > div > a > address")
    if address == None:
        continue
    address = address.getText()

    address_link = fragment_list.select_one(selector="div > div > a").attrs["href"]
    if address_link[0] == "/":
        address_link = "https://www.zillow.com" + address_link

    price = fragment_list.select_one(
        selector="div.StyledPropertyCardDataArea-c11n-8-84-0__sc-yipmu-0.dJxUgr > div > span"
    ).getText()[:6]

    property_detail.append(
        {"address": address, "price": price, "address_link": address_link}
    )


print(*property_detail, sep="\n")

driver = webdriver.Chrome(
    executable_path="....../webdriver/chromedriver.exe", options=chrome_options
)

sf_renting_research = driver.get(form_link)

for property in property_detail:
    sleep(1)
    address_q = driver.find_element(
        By.XPATH,
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    address_q.click()
    address_q.send_keys(property["address"])

    price_q = driver.find_element(
        By.XPATH,
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    price_q.click()
    price_q.send_keys(property["price"])

    address_link_q = driver.find_element(
        By.XPATH,
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    address_link_q.click()
    address_link_q.send_keys(property["address_link"])

    submit = driver.find_element(
        By.XPATH,
        "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span",
    )
    submit.click()

    sleep(1)
    another_response = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
    )
    another_response.click()
