from time import sleep
import pyautogui as pg
from faker import Faker
# from random import choice

fa = Faker()
sleep(5)
for i in range(10):
    pg.write(f"hello {fa.name_male()}")
    # sleep(0.5)
    pg.press("Enter")
