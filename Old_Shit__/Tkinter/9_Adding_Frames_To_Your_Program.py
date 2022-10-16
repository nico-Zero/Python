from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))
# root.iconbitmap("@/media/zero/Software/__/Python/Tkinter/png icon/icons8-vk-com-500.xbm")

# frame = LabelFrame(root, text= "This is my Frame...", padx= 30, pady= 30)
frame = LabelFrame(root, padx= 30, pady= 30)
frame.pack(padx= 10, pady= 10)

b = Button(frame, text= "Don't click Here!")
b.grid(row= 0, column= 0)

b1 = Button(frame, text= "or here...!")
b1.grid(row= 1, column= 1)


root.mainloop()
