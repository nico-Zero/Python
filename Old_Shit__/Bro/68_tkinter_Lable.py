from tkinter import *

window = Tk()
# window.geometry("200x200")
photo = PhotoImage(file="/media/zero/Software/__/Python/Pygame/64pix_bullet/png/021-nuclear-bomb-3.png")

label = Label(
    window,
    text="Hello World!!!",
    bg="#893456",
    font=("Arial", 20, "bold"),
    fg="#440044",
    relief=RAISED,
    bd = 3,
    padx=20,
    pady=20,
    image = photo,
    compound='bottom'
)

label.pack()
# label.place(x=100,y=100)

window.mainloop()
