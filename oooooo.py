from time import sleep
import pyautogui
from faker import Faker

sleep(5)
x = Faker()


for i in range(1000):
    pyautogui.typewrite(x.name())  # type: ignore
    pyautogui.press("enter")
