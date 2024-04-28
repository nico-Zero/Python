from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from os import system


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(
        self,
        down=150,
        up=10,
        twitter_email="zandaxheart955@gmail.com",
        twitter_pass="Nico_Zero##(69)",
        twitter_name="@Zanda0690",
    ):
        self.PROMISED_UP_SPEED = up
        self.PROMISED_DOWN_SPEED = down
        self.TWITTER_EMAIL = twitter_email
        self.TWITTER_PASSWORD = twitter_pass
        self.TWITTER_USERNAME = twitter_name
        self.CURRENT_DOWNLOAD_SPEED = None
        self.CURRENT_UP_SPEED = None

    def get_internet_speed(self):
        driver = webdriver.Chrome(options=chrome_options)
        internet_speed = driver.get("https://www.speedtest.net/")

        sleep(1)
        driver.find_element(
            By.XPATH, "//span[@class='start-text' and text()='Go']"
        ).click()
        for i in range(1, 50):
            print(i)
            sleep(1)
            system("cls")

        print("Found Current Internet speed.")
        download_speed = float(
            driver.find_element(
                By.XPATH,
                "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span",
            ).text
        )
        up_speed = float(
            driver.find_element(
                By.XPATH,
                "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span",
            ).text
        )
        self.CURRENT_DOWNLOAD_SPEED = download_speed
        self.CURRENT_UP_SPEED = up_speed
        driver.quit()

        return {"download": download_speed, "upload": up_speed}

    def tweet_at_provider(self):
        driver = webdriver.Chrome(options=chrome_options)
        twitter_bot = driver.get("https://twitter.com/i/flow/login?lang=en")

        sleep(3)
        _input_1 = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input",
        )
        _input_1.click()
        _input_1.send_keys(self.TWITTER_EMAIL)

        sleep(1)
        next = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span",
        ).click()

        try:
            sleep(2)
            username = driver.find_element(
                By.XPATH,
                "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input",
            )
            username.click()
            username.send_keys(self.TWITTER_USERNAME)

            sleep(1)
            next = driver.find_element(
                By.XPATH,
                "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span",
            ).click()

        except:
            pass

        sleep(2)
        _input_2 = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input",
        )
        _input_2.click()
        _input_2.send_keys(self.TWITTER_PASSWORD)

        sleep(1)
        log_in = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span",
        ).click()

        sleep(10)
        tweet = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div",
        )
        tweet.click()
        tweet.send_keys(
            f"""Promised download speed:- {self.PROMISED_DOWN_SPEED} 
Current download speed:- {self.CURRENT_DOWNLOAD_SPEED}
Promised upload speed:- {self.PROMISED_UP_SPEED}
Current upload speed:- {self.CURRENT_UP_SPEED}"""
)

        sleep(1)
        finally_tweet = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span",
        ).click()

        sleep(10)
        driver.quit()


the_bot = InternetSpeedTwitterBot()
speed = the_bot.get_internet_speed()
print(speed.items())
tweet = the_bot.tweet_at_provider()
