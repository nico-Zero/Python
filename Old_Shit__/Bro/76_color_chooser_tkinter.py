from tkinter import *
from tkinter import colorchooser

def click():
    color,colorhex = colorchooser.askcolor()
    print(color)
    print(colorhex)
    w.config(background=colorhex)
    
w = Tk()
w.geometry("400x400")

button = Button(w,text="click me",command=click)
button.pack()

w.mainloop()
