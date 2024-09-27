from tkinter import *

def doSomething(event):
    print(f"You did something!. {event.x},{event.y}")

w = Tk()

# w.bind("<Button-1>",doSomething)
# w.bind("<Button-2>",doSomething)
# w.bind("<Button-3>",doSomething)
# w.bind("<ButtonRelease>",doSomething)
# w.bind("<Enter>",doSomething)
# w.bind("<Leave>",doSomething)
w.bind("<Motion>",doSomething)

w.mainloop()
