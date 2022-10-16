from fileinput import filename
import os
from tkinter import *
from tkinter import filedialog


def open_file(i=None):
    global filepath
    if not i:
        filepath = filedialog.askopenfilename(
            initialdir="/media/zero/Software/__/Python/Bro",
            title="Open file",
            filetypes=(("text files", "*.txt"), ("All files", "*.*")),
        )
        if filepath is None:
            return
        with open(filepath, "r") as f:
            new(f.read())
    else:
        filepath = filedialog.askopenfilename(
            initialdir="/media/zero/Software/__/Python/Bro",
            title="Delete file",
            filetypes=(("text files", "*.txt"), ("All files", "*.*")),
        )
        if filepath is None:
            return
        return filepath

def save(i=None):
    if not i:
        file = filedialog.asksaveasfile(
            initialdir="/media/zero/Software/__/Python/Bro",
            title="Save file",
            filetypes=(
                ("text files", "*.txt"),
                ("HTML", "*.html"),
                ("All files", "*.*"),
            ),
        )
        if file is None:
            return
        file.write(text.get("1.0", END))
        file.close()
    else:
        with open(filepath, "w") as f:
            f.write(text.get("1.0", END))
    win.destroy()


def delete_file():
    # if entry.get() == "":
    #     pass
    # else:
    try:
        open_file("0")
        os.remove(filepath)
    except TypeError:
        pass
    except FileNotFoundError:
        print("File doesn't exist.")

def new(i=None):
    global text
    global win
    win = Tk()
    if i:
        text = Text(win)
        text.pack()
        text.insert("1.0", i)
    else:
        text = Text(win)
        text.pack()

    save_button = Button(win, text="Save", command=lambda: save(i))
    save_button.pack()

    win.mainloop()
    text.delete(0, END)

w = Tk()

create_f = Button(w, text="Create", command=new)
create_f.pack()

open_f = Button(w, text="Open", command=open_file)
open_f.pack()

delete_f = Button(w, text="Delete", command=delete_file)
delete_f.pack()

w.mainloop()
