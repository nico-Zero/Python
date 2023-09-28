# from time import sleep
# import pyautogui as pg
# from faker import Faker
# # from random import choice

# fa = Faker()
# sleep(5)
# for i in range(10):
#     pg.write(f"hello {fa.name_male()}")
#     # sleep(0.5)
#     pg.press("Enter")


import pyttsx3
import speech_recognition as sr
from os import system

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

# text to speech...


class Speak:
    def __init__(self) -> None:
        self.x = None

    def take_command(self):
        if self.x:
            system("cls")
            print(self.x)

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("Recognising....")
            _query = r.recognize_google(audio, language="en-in")
            print(f"user said: {_query}")

        except:
            self.x = "say that again please.."
            self.take_command()


if __name__ == "__main__":
    jj = Speak()
    jj.take_command()
