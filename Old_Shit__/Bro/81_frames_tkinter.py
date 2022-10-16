# 8:15:39
from tkinter import *

w =Tk()
w.geometry("800x800")

frame = Frame(w,bg="pink",bd=3,relief=SUNKEN)
frame.place(x=100,y=100)
Button(frame,text="W",font=("Consolas",20),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",20),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",20),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",20),width=3).pack(side=LEFT)

w.mainloop()
