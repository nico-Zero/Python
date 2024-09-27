from tkinter import *
from turtle import width

item = [
    (1, "Pizza"),
    (2, "Burger"),
    (3, "Pan_Cake"),
    (4, "Kuchi"),
    (5, "Rice_Omlate"),
    (6, "Pich"),
    (7, "Chips_with_Cat-sose"),
    (8, "Gods_Cheese"),
    (9, "The_Nine"),
    (10, "Sun")
]
    
def submit():
    f = []
    for i in listbox.curselection():
        f.insert(i,listbox.get(i))
    print(x:= f"You have ordered:")
    for i in f:
        print(" "*(len(x)),i)

def insert_i():
    no_i = listbox.size()
    e = entry.get()
    e = e.split(",")
    for i in e:
        listbox.insert(no_i,i)
        no_i += 1
    
    listbox.config(height=listbox.size())
    entry.delete(0,END)

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())

w = Tk()
# w.geometry("400x400")

listbox = Listbox(w,bg="#f7ffde",font=("Constantia",15),width=20,selectmode=MULTIPLE)
listbox.pack(anchor="w")

for i in item:
    listbox.insert(*i)

listbox.config(height=listbox.size())

entry = Entry(w)
entry.pack()

subm = Button(w,text="Submit",command=submit)
subm.pack()

insert = Button(w,text="Insert",command=insert_i)
insert.pack()

delete = Button(w,text="delete",command=delete)
delete.pack()

w.mainloop()
