from struct import pack
from tkinter import *

# 6:24: 27
c = 1
def b():
    global c
    label = Label(w, text=f"{c}>>> Hello, Mother fucker.")
    c += 1
    label.pack()

w = Tk()
photo = PhotoImage(file="/media/zero/Software/__/Python/Tkinter/png icon/Favorites/icons8-100.png")
button = Button(w,
                text="Enter", 
                command=b,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()

w.mainloop()
