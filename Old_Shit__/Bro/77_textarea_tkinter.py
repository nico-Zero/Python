from tkinter import *

def click():
    global item
    item = text.get("1.0",END)
    print(item)


w = Tk()

text = Text(w,bg="light yellow",font=("Ink Free",12),height=8,width=20,padx=20,pady=20,fg='purple')
text.pack()
button = Button(w,text="Click me",command=click)
button.pack()

w.mainloop()
