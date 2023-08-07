from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", False)

driver = webdriver.Chrome(options=chrome_options)

data = driver.get(
    "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
)

