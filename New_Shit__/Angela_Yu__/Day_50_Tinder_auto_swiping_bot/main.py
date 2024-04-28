from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)

sleep(2)
data = driver.get("https://tinder.com/app/recs")
driver.find_element(By.XPATH, "//div[text()='Log in']").click()

# clacking if there is more options
sleep(5)
try:
    driver.find_element(By.XPATH, "//button[text()='More Options']").click()
except:
    print("More Options was not found!")
else:
    print("More Options was found!")

sleep(3)
# log in with facebook button
driver.find_element(
    By.XPATH,
    "/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]",
).click()

sleep(2)
windows = driver.window_handles
base_window = windows[0]
facebook_login_window = windows[1]

# switching window to facebook login window
driver.switch_to.window(facebook_login_window)

sleep(2)
# sending log in info
driver.find_element(By.ID, "email").send_keys("yuvrajmahilange955@gmail.com")
driver.find_element(By.ID, "pass").send_keys("7247477955")

sleep(2)
# Logging in
driver.find_element(By.ID, "loginbutton").click()

# Switching back to base window
driver.switch_to.window(base_window)
try:
    sleep(15)
    # Accepting location access
    driver.find_element(
        By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]"
    ).click()

    sleep(1)
    # Decline notification access
    driver.find_element(
        By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]"
    ).click()

    sleep(1)
    # accepting catcher
    driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]",
    ).click()

except:
    print("Error in after login.")

# A loop for Rejecting continually
sleep(10)
for _ in range(100):
    sleep(1)
    try:
        driver.find_element(By.XPATH,"//div[text()='not interested']").click()
    except:
        pass
    else:
        print("Home Screen Addon found")
    sleep(1)
    driver.find_element(
        By.XPATH,
        "//span[@class='D(b) Expand' and @style='transform: scale(1); filter: none;']",
    ).click()