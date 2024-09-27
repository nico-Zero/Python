from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

webdriver_location = "....../webdriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=webdriver_location, options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

first_name = driver.find_element(By.NAME, "FirstName")
last_name = driver.find_element(By.NAME, "LastName")
email = driver.find_element(By.NAME, "Email")
sign_up_button = driver.find_element(By.LINK_TEXT, "Sign Up")

first_name.send_keys("yuvraj")
last_name.send_keys("mahilange")
email.send_keys("znadaxheat955@gmail.com")
sign_up_button.click()


# driver.quit()
