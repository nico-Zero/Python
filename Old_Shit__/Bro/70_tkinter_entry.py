# 6:31:12
from tkinter import *


def print_name(name):
    label = Label(w, text=f"Hello, {name} !!!")
    print(name)
    label.pack()
    entry.config(state=DISABLED)


def Delete():
    entry.delete(0, END)


def Backspace():
    if (entry.get())[-2] == ".":
        entry.delete(len(entry.get()) - 2, END)
    else:
        entry.delete(len(entry.get()) - 1, END)


w = Tk()

entry = Entry(
    w, 
    text="Enter your name...", 
    font=("Arial", 20), 
    fg="#00FF00", 
    bg="black", 
    # show="*"
)
entry.insert(0, "Spangbob")


button = Button(w, text="Enter", command=lambda: print_name(entry.get()))
delete = Button(w, text="Delete", command=Delete)
backspace = Button(w, text="Backspace", command=Backspace)

entry.pack(side=LEFT)
button.pack(side=RIGHT)
delete.pack()
backspace.pack()

w.mainloop()
