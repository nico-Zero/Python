from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Opendilog")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))

frame = LabelFrame(root, padx= 30, pady= 30)
frame.pack(padx= 10, pady= 10)

def open(x):
    global image
    root.filename = filedialog.askopenfilename(initialdir=x, title= "Select A File", filetypes=(("png file","*.png"),("all files","*.*")))
    Label(frame,text=root.filename).pack()
    image = ImageTk.PhotoImage(Image.open(root.filename))
    Label(frame,image=image).pack()

ent = Entry(frame,width=20)
ent.pack()

Button(frame,text= "OK",command= lambda: open(ent.get())).pack()

root.mainloop()
