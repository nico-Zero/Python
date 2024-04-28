from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from random import choice
from time import sleep


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


def form_(amount: int):
    try:
        for i in range(amount):
            print(f"Iteration :- {i}")
            driver.get(
                "https://docs.google.com/forms/d/e/1FAIpQLSeeLGdC2Co8OrEqsQx8ZN5j27GOm6SzXgZT7GnIoFk7C_rdEg/viewform?usp=sf_link"
            )

            all_elements = driver.find_elements(By.CLASS_NAME, r"Qr7Oae")
            print(len(all_elements))
            submit = driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span",
            )

            sleep(0.5)
            for element in all_elements:
                span_list = element.find_elements(By.CLASS_NAME, r"aDTYNe")
                choice(span_list).click()

            submit.click()
    except Exception as e:
        print(e)
        return None
    else:
        return True


def run(amount: int):
    while 1:
        x = form_(amount)
        if x == None:
            continue
        else:
            break


run(300)
