from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Image")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))

frame = LabelFrame(root, padx= 30, pady= 30)
frame.pack(padx= 10, pady= 10)

# showinfo , showwarning, showerror, askquestion, askokcancel, askyesno.

def Popup():
    # r =  messagebox.showinfo("This is my Popup!", "showinfo")
    # r =  messagebox.showwarning("This is my Popup!", "showwarning")
    r =  messagebox.showerror("This is my Popup!", "showerror")
    # r =  messagebox.askquestion("This is my Popup!", "askquestion")
    # r =  messagebox.askokcancel("This is my Popup!", "askokcancel")
    # r =  messagebox.askyesno("This is my Popup!", "askyesno")

    # Label(frame,text= r).pack()

    if r == 1 :
        Label(frame,text= "Go Ahead!").pack()
    elif r == 0:
        Label(frame,text= "Stop!").pack()
        
Button(frame, text= "Popup", command=Popup).pack()

root.mainloop()

