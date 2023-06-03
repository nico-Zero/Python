from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from os import system


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    executable_path="....../webdriver/chromedriver.exe", options=chrome_options
)

target_account = input("Enter the target account name:- ")
if target_account == "":
    target_account = "helenyarmak"

instagram = driver.get("https://www.instagram.com/")

sleep(3)
email_input = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input",
)
email_input.click()
email_input.send_keys("nobodyben60@gmail.com")

sleep(1)
password_input = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input",
)
password_input.click()
password_input.send_keys("nicozero@69$$_ż")

sleep(1)
log_in = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button",
).click()

sleep(4)
driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div",
).click()

sleep(2)
driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
).click()

sleep(2)
driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div",
).click()

sleep(2)
search_input = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input",
)
search_input.click()
search_input.send_keys(target_account)
search_input.send_keys(Keys.ENTER)

sleep(2)
driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div/span[1]/span/div/span",
).click()

sleep(2)
driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a",
).click()

# finding_account_list
sleep(5)
account_list = driver.find_elements(
    By.XPATH,
    "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div",
)

print(f"Total Account found:- {len(account_list)}")
# Following account
for account in account_list:
    sleep(1)
    follow = account.find_element(By.TAG_NAME, "button")
    follow.click()

driver.quit()
