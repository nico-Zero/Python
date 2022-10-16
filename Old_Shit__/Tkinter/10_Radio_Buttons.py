from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))

frame = LabelFrame(root, padx= 30, pady= 30)
frame.pack(padx= 10, pady= 10)


# r = IntVar()
r = StringVar()
r.set("")

def clicked(value):
    if value == "":
        pass
    else:
        Label(frame, text= value).pack(anchor=W)
    
modes = [
    ("Pepperaoni","Pepperaoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]
     
# for i in range(1,11):
#     Radiobutton(frame, text= f"Option {i}", variable=r, value=i).pack()

for i,j in modes:
    Radiobutton(frame, text= f"Option {i}", variable=r, value=j).pack(anchor=W)


Button(frame,text="Click",command= lambda: clicked(r.get())).pack()


root.mainloop()
