from tkinter import *
from time import *

def doSomething(event):
    l.config(text=f"{event.keysym}")

w = Tk()
w.geometry("250x250")

w.bind("<Key>",doSomething)
l = Label(w,font=("Arial",100))
l.pack()

w.mainloop()

