from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from os import system


class InstaFollower:
    def __init__(
        self,
        email="nobodyben60@gmail.com",
        password="nicozero@69$$_ż",
        target_account=input("Enter the target account name:- "),
    ):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        if target_account == "":
            self.Target_account = "helenyarmak"
        else:
            self.Target_account = target_account

        self.DRIVER = webdriver.Chrome(options=chrome_options)

        self.Email_ID = email
        self.Password = password
        self.Found_Account_list = []

    def login(self):
        instagram = self.DRIVER.get("https://www.instagram.com/")

        sleep(3)
        email_input = self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input",
        )
        email_input.click()
        email_input.send_keys(self.Email_ID)

        sleep(1)
        password_input = self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input",
        )
        password_input.click()
        password_input.send_keys(self.Password)

        sleep(1)
        log_in = self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button",
        ).click()

    def find_followers(self):
        sleep(4)
        self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div",
        ).click()

        sleep(2)
        self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
        ).click()

        sleep(2)
        self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div",
        ).click()

        sleep(2)
        search_input = self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input",
        )
        search_input.click()
        search_input.send_keys(self.Target_account)
        search_input.send_keys(Keys.ENTER)

        sleep(2)
        self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div/span[1]/span/div/span",
        ).click()

        sleep(2)
        self.DRIVER.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a",
        ).click()

        # finding_account_list
        sleep(5)
        account_list = self.DRIVER.find_elements(
            By.XPATH,
            "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div",
        )
        self.Found_Account_list = account_list
        print(f"Total Account found:- {len(account_list)}")

    def follow(self, account_list=None):
        for account in account_list or self.Found_Account_list:
            sleep(1)
            _follow = account.find_element(By.TAG_NAME, "button")  # type: ignore
            _follow.click()

    def quit(self):
        self.DRIVER.quit()


insta_following_bot = InstaFollower()
insta_following_bot.login()
insta_following_bot.find_followers()
insta_following_bot.follow()
insta_following_bot.quit()
