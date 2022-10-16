from curses import window
from tkinter import *

from pyparsing import col
from sqlalchemy import column

def save():
    l = [entry1.get(), entry2.get(), entry3.get(), entry4.get()]
    for i in l:
        print(i)

window = Tk()

w = Frame(window)
w.pack(side=TOP,expand=True,fill="both")

entry1 = Entry(w)
entry1.grid(column=1, row=0)
Label(w, text="Name:").grid(column=0, row=0)

entry2 = Entry(w)
entry2.grid(column=1, row=1)
Label(w, text="Age").grid(column=0, row=1)

entry3 = Entry(w)
entry3.grid(column=1, row=2)
Label(w, text="Gender").grid(column=0, row=2)

entry4 = Entry(w)
entry4.grid(column=1, row=3)
Label(w, text="Grade").grid(column=0, row=3)

button = Button(w,text="Save",command=save)
button.grid(columnspan=2,column=0,row=4)

window.mainloop()
