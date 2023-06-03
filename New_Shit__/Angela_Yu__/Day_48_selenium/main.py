from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver_path = "....../webdriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.get(
    "https://www.amazon.in/gp/product/B07FTZ259M/ref=ewc_pr_img_1?smid=A3LD4MMBBTHP7M&psc=1"
)

# driver.get("https://www.python.org/")

price = driver.find_element(By.CLASS_NAME, "a-price-whole").text.replace(",", "")
print(int(price))

# input_ = driver.find_element(By.NAME, "q")
# print(input_.get_attribute("placeholder"))

# python_logo = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(python_logo.get_attribute("href"))

# submit_bug = driver.find_elements(
#     By.XPATH, r"/html/body/div/footer/div[2]/div/ul/li[3]/a"
# )
# for submit in submit_bug:
#     print(submit.get_attribute("href"))


driver.quit()
