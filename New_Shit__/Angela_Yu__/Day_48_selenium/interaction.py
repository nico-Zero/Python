from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

webdriver_location = "....../webdriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=webdriver_location, options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number = driver.find_element(By.CSS_SELECTOR, "#articlecount > a:nth-child(1)")
# number.click()

# int_num = int(number.text.replace(",", ""))
# print(int_num)

# history = driver.find_element(By.LINK_TEXT, "View history")
# history.click()

search_box = driver.find_element(By.LINK_TEXT, r"Search")
search_box.click()
input_box = driver.find_element(By.NAME, "search")
input_box.send_keys("Python")
input_box.send_keys(Keys.ENTER)

# driver.quit()
