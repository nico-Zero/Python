from faker import Faker
from os import system
import tkinter

system("cls")


# tkinter window
window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=800, height=600)

# Label from tkinter
label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
label.pack()

label["text"] = "Fuck you"
label.config(text="He-He")

# function for clicking the button
def click(x):
    if x == "clear":
        system("cls")
        return None

    print(f"☠️ 𒓋  {x}")
    label["text"] = x


# entry area
entry = tkinter.Entry(width=20)
entry.insert(tkinter.END, string="clear")
entry.pack()

# Button from tkinter
button = tkinter.Button(text="Click Me", command=lambda: click(entry.get()))
button.pack()

# Text area from tkinter
text = tkinter.Text(height=5, width=25)
text.focus()
text.insert(tkinter.END, "multi-line text_area.")
print(text.get("1.0", tkinter.END))
text.pack()

# a Function for spinb Object
def spinbox():
    print(spinb.get())


# spinbox from tkinter
spinb = tkinter.Spinbox(from_=0, to=10, width=10, command=spinbox)
spinb.pack()

# ss function for scale object
def ss(value):
    print(value)


# Scale from tkinter
scale = tkinter.Scale(from_=0, to=1000, width=10, command=ss)
scale.pack()

# state function for seeing the state of checkbutton.
def state():
    print(check_state.get())


# checkbutton from tkinter
check_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Fuck ?", variable=check_state, command=state)
check_state.get()
checkbutton.pack()

# r_state function for checking the state of radiobuttons
def r_state():
    print(radio_state.get())


# radiobutton from tkinter
radio_state = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(
    text="Radiobutton 1", value=1, variable=radio_state, command=r_state
)
radiobutton2 = tkinter.Radiobutton(
    text="Radiobutton 2", value=2, variable=radio_state, command=r_state
)
radiobutton1.pack()
radiobutton2.pack()

# to print out listbox info
def listbox_used(e):
    print(listbox.get(listbox.curselection()))

# listbox from tkinter
listbox = tkinter.Listbox(height=6)
name = Faker()
hitman = [name.name() for i in range(10)]

for i in hitman:
    listbox.insert(hitman.index(i), i)
    
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
