import pyautogui
from time import sleep

sleep(5)


for _ in range(10):
    pyautogui.write("hello world")
    pyautogui.press("enter")
