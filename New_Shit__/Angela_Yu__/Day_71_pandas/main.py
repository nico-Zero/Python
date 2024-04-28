from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
)

total_elements = []
last_page = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div[1]/article/div[3]/a[6]/div"
)

columns_names = []
for column in driver.find_elements(By.TAG_NAME, "th"):
    columns_names.append(column.text)
columns_names.remove("")

with open("collage_data.csv", "a", newline='', encoding='utf-8') as file:
    csvwriter = csv.writer(file, delimiter=",")
    csvwriter.writerow(columns_names)

for i in range(int(last_page.text)):
    table_elements = driver.find_elements(By.CLASS_NAME, "data-table__row")
    for element in table_elements:
        data = element.find_elements(By.CLASS_NAME, "data-table__value")
        dd = [i.text for i in data if i.text != ""]
        with open("collage_data.csv", "a", newline='', encoding='utf-8') as file:
            csvwriter = csv.writer(file, delimiter=",")
            csvwriter.writerow(dd)
        print(dd)
    sleep(1)
    next = driver.find_element(
        By.CLASS_NAME,
        "icon-right-open",
    )
    next.click()
    sleep(1)
