from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("HeHe")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))

frame = LabelFrame(root, padx= 30, pady= 30)
frame.pack(padx= 10, pady= 10)

def new_w():
    global ima
    top = Toplevel()
    top.title("Booooooooooooooooooooooom")
    top.iconbitmap("@/media/zero/Software/__/Python/Tkinter/png icon/icons8-vk-com-500.xbm")
    ima = ImageTk.PhotoImage(Image.open("/media/zero/Software/__/Python/Tkinter/wifi-router.png"))
    Label(top, image=ima).pack()
    Button(top, text= "Close Window", command= top.destroy).pack()

Button(frame, text= "New Window", command= new_w).pack()


root.mainloop()
