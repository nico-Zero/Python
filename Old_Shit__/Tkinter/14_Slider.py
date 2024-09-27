from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Opendilog")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))
root.geometry("500x500")

frame = LabelFrame(root, padx= 30, pady= 30,)
frame.grid(row = 0, column= 0,padx= 10, pady= 10)

def vir():
    Label(frame,text=vertical.get()).pack()
def hir():
    Label(frame,text=horizantal.get()).pack()
def geo(var):
    if horizantal.get() > 200 and vertical.get() > 200:
        root.geometry(f"{horizantal.get()}x{vertical.get()}")
    
vertical = Scale(frame,from_=0,to=600,command=geo)
vertical.pack()
Button(frame,text="Click Me",command=vir).pack()

horizantal = Scale(frame,from_=0,to=600, orient= HORIZONTAL,command=geo)
horizantal.pack()
Button(frame,text="Click Me",command=hir).pack()
Button(frame,text="Resize!",command=lambda: geo(0)).pack()

root.mainloop()
