from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Opendilog")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))
root.geometry("300x300")

frame = LabelFrame(root, padx= 30, pady= 30,)
frame.grid(row = 0, column= 0,padx= 10, pady= 10)

def check():
    Label(frame,text= var.get()).pack()

var = StringVar()
c = Checkbutton(frame,text="Check this box i dare you!", variable=var,onvalue="On",offvalue="Off",command= check)
c.deselect()
c.pack()


root.mainloop()
