from tkinter import *
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(
        initialdir="/media/zero/Software/__/Python/Bro", title="Open file",filetypes=(("text files","*.txt"),("All files","*.*"))
    )
    with open(filepath, "r") as f:
        print(f.read())


w = Tk()

button = Button(w, text="Open", command=open_file)
button.pack()
 
w.mainloop()
