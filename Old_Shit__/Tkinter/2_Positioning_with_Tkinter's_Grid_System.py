from tkinter import *

root = Tk()

# Creating a Lable Widget
mylabel1 = Label(root, text = "Hello Boyi!")
mylabel2 = Label(root, text = "My Name Is Jhon Elder")

# Shoving it onto the screen
mylabel1.grid(row= 0, column= 0)
mylabel2.grid(row= 2, column= 2)

root.mainloop()