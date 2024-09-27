from tkinter import *

x = False

def some(event):
    widget = event.widget
    x = widget.winfo_x()-widget.startX + event.x
    y = widget.winfo_y()-widget.startY + event.y
    widget.place(x=x,y=y)

def T(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

w = Tk()
w.geometry("600x600")

# w.bind("<Motion>",some)
# w.bind("<Button-1>",T)
# w.bind("<ButtonRelease>",F)

lable1 = Label(w,bg="black",width=20,height=10)
lable1.place(x=0,y=0)
lable1.bind("<Button-1>",T)
lable1.bind("<B1-Motion>",some)

lable2 = Label(w,bg="red",width=20,height=10)
lable2.place(x=100,y=100)
lable2.bind("<Button-1>",T)
lable2.bind("<B1-Motion>",some)

w.mainloop()
# 9:11:10