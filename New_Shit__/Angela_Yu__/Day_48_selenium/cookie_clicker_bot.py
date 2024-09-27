from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import time
from os import system


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

data = driver.get("https://orteil.dashnet.org/experiments/cookie/")

big_cookie = driver.find_element(By.ID, "cookie")

items = [i.text.split(" - ") for i in driver.find_elements(By.CSS_SELECTOR, "#store b")]
items = {
    i: j
    for i, j in zip(
        ["buy" + i[0] for i in items[:-1]],
        [int(i[1].replace(",", "")) for i in items[:-1]],
    )
}

timeout = time() + 5
die = time() + 60 * 5

while 1:
    big_cookie.click()
    if time() > timeout:
        system("cls")
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        print("Money:- ", money)
        perfect_upgrade = max([i for i in items.values() if i < money])
        item = [i for i, j in items.items() if j == perfect_upgrade]
        print(item)
        upgrade = driver.find_element(By.ID, item[0])
        upgrade.click()

        timeout = time() + 5
    if time() > die:
        print(driver.find_element(By.ID, "cps").text)
        break
