import shutil
import os
from tkinter import *
from tkinter import filedialog

def open_file():
    global text,filepath
    filepath = filedialog.askopenfilename(
        initialdir="/media/zero/Software/__/Python/Bro",
        title="Delete file",
        filetypes=(("text files", "*.txt"), ("All files", "*.*")),
    )
    if filepath is None:
        return

    text = Text(w)
    text.pack()

    with open(filepath,"r+") as f:
        text.insert(1.0,f.read())
    
def save_file():
    with open(filepath,"w+") as f:
        f.write(text.get(1.0,END))

def close():
    try:
        text.destroy()
    except NameError:
        pass

def cut ():
    global cut_name
    cut_name = filedialog.askopenfilename(
        initialdir="/media/zero/Software/__/Python/Bro",
        title="Copy file",
        filetypes=(("text files", "*.txt"), ("All files", "*.*"))
    )
def copy ():
    global cf_name
    cf_name = filedialog.askopenfilename(
        initialdir="/media/zero/Software/__/Python/Bro",
        title="Copy file",
        filetypes=(("text files", "*.txt"), ("All files", "*.*"))
    )

cut_name = None
cf_name = None

def paste ():
    if cf_name :
        p_name = filedialog.askdirectory(
            initialdir="/media/zero/Software/__/Python/Bro",
            title="Paste file"
        )

        shutil.copyfile(cf_name,p_name)
        print("Done...")
    
    
    if cut_name:
        p_name = filedialog.askdirectory(
            initialdir="/media/zero/Software/__/Python/Bro",
            title="Paste file"
        )
        try:
            if os.path.exists(p_name):
                print("There is already a file there...")
            else:
                os.replace(cut_name,p_name)
                print(p_name,"was moved...")
        except FileNotFoundError:
            print('Source was not found...')


w = Tk()
w.geometry("520x420")
# PhotoImage for menu icons
photo1 = PhotoImage(file="/media/zero/Software/__/Python/Pygame/32pix_bullet/png/015-atom-1.png")
photo2 = PhotoImage(file="/media/zero/Software/__/Python/Pygame/32pix_bullet/png/011-nuclear-explosion.png")
photo3 = PhotoImage(file="/media/zero/Software/__/Python/Pygame/32pix_bullet/png/013-nuclear.png")
photo4 = PhotoImage(file="/media/zero/Software/__/Python/Pygame/32pix_bullet/png/014-nuclear-sign.png")

menubar = Menu(w)
w.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label = "File",menu = filemenu)
filemenu.add_command(label = "Open",image= photo1,compound=LEFT,command=open_file)
filemenu.add_command(label = "Save",image= photo2,compound=LEFT,command=save_file)
filemenu.add_separator()
filemenu.add_command(label = "Close",image= photo4,compound=LEFT,command=close)
filemenu.add_command(label = "Exit",image= photo3,compound=LEFT,command=quit)

editmenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label = "Edit",menu = editmenu)
editmenu.add_command(label = "Cut",image= photo1,compound=LEFT,command=cut)
editmenu.add_command(label = "Copy",image= photo2,compound=LEFT,command=copy)
editmenu.add_separator()
editmenu.add_command(label = "Paste",image= photo3,compound=LEFT,command=paste)

w.mainloop()
