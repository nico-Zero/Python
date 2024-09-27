from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver_path = "....../webdriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.get("https://www.python.org/")

time = driver.find_elements(
    By.CSS_SELECTOR, ".event-widget time"
)
detail = driver.find_elements(
    By.CSS_SELECTOR, ".event-widget li a"
)

upcoming_event_time = [i.get_attribute("datetime").split("T")[0] for i in time]
upcoming_event_detail = [i.text for i in detail]

filtered_data = {
    k: {"time": i, "name": j}
    for k, i, j in zip(
        range(len(upcoming_event_time)), upcoming_event_time, upcoming_event_detail
    )
}

print(filtered_data)
