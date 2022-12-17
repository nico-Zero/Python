from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import time
from os import system


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)

data = driver.get(
    "https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fin%2Elinkedin%2Ecom%2Fin%2Fyuvraj-mahilange-91097a248&fromSignIn=true&trk=public_profile_nav-header-signin"
)

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
signin = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

username.send_keys("zandaXheart955@gmail.com")
password.send_keys("nicozero")

signin.click()
print("login successful")
