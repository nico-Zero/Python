from tkinter import *
from tkinter import ttk

w = Tk()
w.geometry("500x500")

notebook = ttk.Notebook(w)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,fill="both" )

Label(tab1,text="Hello, this is tab1.").pack()
Label(tab2,text="Good Bye, this is tab2.").pack()

w.mainloop()
