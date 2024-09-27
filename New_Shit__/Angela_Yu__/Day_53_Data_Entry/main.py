from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
from time import sleep


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

form_link = "https://docs.google.com/forms/d/e/1FAIpQLScJXp_yzZ6mOH7QtZUdub0mMvfyXyfdDCvtn4wZPEbF-hawqw/viewform?usp=sf_link"

zillow_link = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.8834888362371%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.666936495460185%2C%22west%22%3A-122.63417331103516%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept-Language": "en-US,en;q=0.5",
}

zillow_data = requests.get(url=zillow_link, headers=header)
zillow_data.raise_for_status()
data = zillow_data.text

# with open("index.html", "w") as index:
#     index.write(data)

soup = BeautifulSoup(data, "html.parser")
data_list = soup.find_all(
    name="li",
    class_="ListItem-c11n-8-84-0__sc-10e22w8-0 StyledListCardWrapper-srp__sc-wtsrtn-0 cTMokP gTOWtl",
)

print(f"Total Property Found:- {len(data_list)}")
print(*data_list, sep="\n")
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

driver = webdriver.Chrome(options=chrome_options)

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
