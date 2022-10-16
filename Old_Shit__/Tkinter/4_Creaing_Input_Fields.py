from tkinter import *
from turtle import width

root = Tk()

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

e = Entry(root, width= 25 )
e.pack()
e.insert(0, "Enter your name ")

myButton = Button(root, text="Enter your name: ", command=myClick, fg= "blue", bg= "pink")  

myButton.pack()

root.mainloop()
