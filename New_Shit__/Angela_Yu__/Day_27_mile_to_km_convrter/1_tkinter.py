from os import system
import tkinter

system("cls")

# function for clicking the button
def click(x):
    if x == "clear":
        system("cls")
        return None

    print(f"☠️ 𒓋  {x}")
    label["text"] = x

# tkinter window
window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=800, height=600)

# Label from tkinter
label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
label["text"] = "Fuck you"
label.config(text="He-He")
label.grid(row=0,column=0)

# Button from tkinter
button = tkinter.Button(text="Click Me", command=lambda: click(entry.get()))
button.grid(row=1,column=1)

# second Button from tkinter
button = tkinter.Button(text="Click Me", command=lambda: click(entry.get()))
button.grid(row=0,column=2)

# entry area
entry = tkinter.Entry(width=20)
entry.insert(tkinter.END, string="clear")
entry.grid(row=3,column=4)

window.mainloop()
