from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from os import system


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)

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


sleep(15)


job = driver.find_element(
    By.CSS_SELECTOR, "#global-nav > div > nav > ul > li:nth-child(3) > a"
)
job.click()

sleep(5)

python_developer_job = driver.find_element(By.ID, "recentSearchesIndex__0")
python_developer_job.click()

sleep(3)

easy_apply = job.find_element(By.XPATH, '//button[text()="Easy Apply"]')
easy_apply_on_or_off = easy_apply.get_attribute("aria-checked")

if easy_apply_on_or_off == "false":
    filter = driver.find_element(
        By.XPATH,
        "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/div/div/button",
    )
    filter.click()

    sleep(2)

    easy_apply = driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div/div[2]/ul/li[9]/fieldset/div/div"
    )
    easy_apply.click()

    sleep(1)

    apply_filter = driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div/div[3]/div/button[2]"
    )
    apply_filter.click()


sleep(5)

jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for job_x in jobs:
    sleep(3)
    print(job_x)
    job_x.click()
    driver.find_element(
        By.XPATH, '//span[@class="artdeco-button__text" and text()="Easy Apply"]'
    ).click()
    driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input",
    ).send_keys("7247477955")

    sleep(3)

    driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button",
    ).click()
