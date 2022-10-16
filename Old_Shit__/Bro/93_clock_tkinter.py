from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    t.config(text=time_string)
    day_string = strftime("%A")
    d_w.config(text=day_string)
    date_string = strftime("%B-%d-%Y")
    d.config(text=date_string)
    
    w.after(1000,update)

w = Tk()
w.config(bg="black")

t = Label(w,font=("Arial",50),fg="#00FF00",bg="black")
t.pack() 
d = Label(w,font=("Arial",25),fg="#86007a",bg="black")
d.pack() 
d_w = Label(w,font=("Ink Free",20),fg="pink",bg="black")
d_w.pack()

update()

w.mainloop()
