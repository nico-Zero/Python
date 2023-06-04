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

# driver = webdriver.Chrome(
#     executable_path="....../webdriver/chromedriver.exe", options=chrome_options
# )

form_link = "https://docs.google.com/forms/d/e/1FAIpQLScJXp_yzZ6mOH7QtZUdub0mMvfyXyfdDCvtn4wZPEbF-hawqw/viewform?usp=sf_link"
zillow_link = r"https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.8834888362371%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.666936495460185%2C%22west%22%3A-122.63417331103516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

zillow_data = requests.get(zillow_link)
zillow_data.raise_for_status()
zillow_data = zillow_data.text

# paresed_zillow_data = BeautifulSoup(zillow_data, "html.parser")
# data = paresed_zillow_data.find_all(
#     name="li",
#     class_="ListItem-c11n-8-84-0__sc-10e22w8-0 StyledListCardWrapper-srp__sc-wtsrtn-0 cTMokP gTOWtl",
# )

# filtered_data = []


# for fragment in data:
#     address = fragment.select_one(selector=r"#zpid_37\.779613--122\.40396 > div > div.StyledPropertyCardDataWrapper-c11n-8-84-0__sc-1omp4c3-0.cXTjvn.property-card-data > a > address").getText()
#     print(address)

