from tkinter import *
from tkinter import messagebox

def click():
    # while True:
        # messagebox.showinfo(title='this is an info messagebox.',message="You are a person.")
        # messagebox.showwarning(title='This is an info messagebox.',message="You are a person.")
        # messagebox.showerror(title='this is an info messagebox.',message="You are a person.")

        # if messagebox.askokcancel(title='this is an info messagebox.',message="You are a person."):
        #     print("You did a thing.")
        # else:
        #     print("No we didn't.")

        # if messagebox.askretrycancel(title='this is an info messagebox.',message="You are a person."):
        #     print("You retried the thing.")
        # else:
        #     print("No You didn't retried the thing.")
        
        # if messagebox.askyesno(title='this is an info messagebox.',message="You are a person."):
        #     print("Ohhh Yaaaa.")
        # else:
        #     print("Hell naa man.")

        # a = messagebox.askquestion(title="ask quistion.",message="Do you like pie?")
        # if(a == "yes"):
        #     print("Yes i like pie.")
        # else:
        #     print("No i don't like pie.")

        a = messagebox.askyesnocancel(title="ask quistion.",message="Do you like pie?",icon='info')
        if a == None:
            print("You Canceled it.")
        elif a:
            print("Yes i like pie.")
        else :
            print("No i don't like it.") 

w = Tk()

button = Button(w,text="OK",command=click)
button.pack()

w.mainloop()
