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
        up=150,
        down=10,
        twitter_email="zandaxhearrt955@gmail.com",
        twitter_pass="Nico_Zero##(69)",
    ):
        self.DRIVER = webdriver.Chrome(
            executable_path="....../webdriver/chromedriver.exe", options=chrome_options
        )

        self.PROMISED_UP_SPEED = up
        self.PROMISED_DOWN_SPEED = down
        self.TWITTER_EMAIL = twitter_email
        self.TWITTER_PASSWORD = twitter_pass
        self.CURRENT_DOWNLOAD_SPEED = None
        self.CURRENT_UP_SPEED = None

    def get_internet_speed(self):
        internet_speed = self.DRIVER.get("https://www.speedtest.net/")
        self.DRIVER.find_element(
            By.XPATH, "//span[@class='start-text' and text()='Go']"
        ).click()
        for i in range(1, 60):
            print(i)
            sleep(1)
            system("cls")

        print("Found Current Internet speed.")
        download_speed = float(self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span",
        ).text)
        up_speed = float(self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span",
        ).text)
        self.CURRENT_DOWNLOAD_SPEED = download_speed
        self.CURRENT_UP_SPEED = up_speed
        return {"download" : download_speed, "upload" : up_speed}

    def tweet_at_provider(self):
        pass


the_bot = InternetSpeedTwitterBot()
speed = the_bot.get_internet_speed()
print(speed.values())
