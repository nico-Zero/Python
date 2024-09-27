import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def color_change():
    color = colorchooser.askcolor(title="Choose a color or leave.")
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))

def new():
    w.title("Untitled")
    text_area.delete(1.0, END)


def open_f():
    file = askopenfilename(
        initialdir="/media/zero/Software/__/Python",
        defaultextension=".txt",
        title="Open File",
        filetypes=[("All files", "*.*"), ("Python", "*.py"), ("Text", "*.txt")],
    )
    try:
        w.title(os.path.basename(file))
        text_area.delete(1.0, END)
        with open(file, "r") as f:
            text_area.insert(1.0, f.read())
    except Exception as e:
        print(e)


def save():
    file = asksaveasfilename(
        initialfile="/media/zero/Software/__/Python",
        defaultextension=".txt",
        title="Save File",
        filetypes=[("All files", "*.*"), ("Python", "*.py"), ("Text", "*.txt")],
    )
    if file is None:
        return
    else:
        try:
            with open(file,'w') as f:
                f.write(text_area.get(1.0,END))
        except:
            pass
def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this program.", "This is a program...")


w = Tk()
w.title("Text Editor")
file = None

w_width = 600
w_height = 600

screen_w = w.winfo_screenwidth()
screen_h = w.winfo_screenheight()

x = int((screen_w / 2) - (w_width / 2))
y = int((screen_h / 2) - (w_height / 2))

w.geometry(f"{w_width}x{w_height}+{x}+{y}")

font_name = StringVar(w)
font_name.set("Arial")

font_size = StringVar(w)
font_size.set("25")

text_area = Text(w, font=(font_name.get(), font_size.get()))
scrollbar = Scrollbar(text_area)

w.grid_rowconfigure(0, weight=1)
w.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + W + S)

scrollbar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scrollbar.set)

frame = Frame(w)
frame.grid()

color_button = Button(frame, text="Color", command=color_change)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *(font.families()[:40]), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, text=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(w)
w.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open_f)
file_menu.add_command(label="Save", command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

w.mainloop()
