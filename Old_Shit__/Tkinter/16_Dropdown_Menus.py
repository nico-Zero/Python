from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Opendilog")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))
root.geometry("400x400")

frame = LabelFrame(root, padx= 30, pady= 30,)
frame.grid(row = 0, column= 0,padx= 10, pady= 10)

#Drop down box
def put():
    Label(root,text=x.get()).grid(row=2,column=0)

x = StringVar()
options = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
x.set(options[0])
drop = OptionMenu(frame,x,*options)
drop.grid(row=0,column=0)

Button(frame,text="Click Me!",command= put).grid(row=1,column=0)


root.mainloop()
