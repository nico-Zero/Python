from keybind import KeyBinder
import schedule
import time
from sys import exit
from os import system

class Good:
    def __init__(self):
        self.__gg = ""

    def addShip(self, value):
        self.__gg += value

    def down(self):
        self.__gg = "\n" + self.__gg
        self.getShip()

    def up(self):
        if not self.__gg[0].isalpha():
            splited_gg = list( self.__gg )
            self.__gg = "".join(splited_gg[1:])
        self.getShip()

    def right(self):
        splited_gg = self.__gg.split("\n")
        splited_gg[-1] = " " + splited_gg[-1]
        self.__gg = "\n".join(splited_gg)
        self.getShip()

    def left(self):
        splited_gg = self.__gg.split("\n")
        if not splited_gg[-1][0].isalpha():
            splited_gg[-1] = splited_gg[-1][1:]
            self.__gg = "\n".join(splited_gg)
        self.getShip()

    def getShip(self):
        system("clear")
        print(self.__gg)

system("clear")
gg = Good()
gg.addShip(input("Enter the Ship:- "))
gg.getShip()
jj = False

KeyBinder.activate({

    'k': gg.up,
    'j': gg.down,
    'l': gg.left,
    'h': gg.right,
    'Ctrl-K': exit,

}, run_thread=True)

def do_something(x = None):
    global jj
    jj =True
    # if x is None:
    #     print("Hello, World!!!")
    #     jj = True
    # else:
    #     print(f"Hello, {x}")
    #     jj = False

schedule.every(10).seconds.do(do_something)

while True:
    schedule.run_pending()
    if jj:
        system("clear")
        break
