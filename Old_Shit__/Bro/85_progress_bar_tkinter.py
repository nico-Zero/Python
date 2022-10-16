from tkinter import *
from tkinter.ttk import *
import time

def start():
    task = 100
    x = 0
    speed = 0.05
    while(x<task):
        time.sleep(speed)
        bar["value"]+=1
        x+=1
        text.set(f"{x}/{task} GB completed :)")
        percent.set(f"{int((x/task)*100)}%")
        speed += 0.001
        w.update_idletasks()
        
w = Tk()

percent = StringVar()
text = StringVar()


bar = Progressbar(w,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

p_lable = Label(w,textvariable=percent)
p_lable.pack()
t_lable = Label(w,textvariable=text)
t_lable.pack()

button = Button(w,text="Dowmload",command= start).pack()

w.mainloop()

