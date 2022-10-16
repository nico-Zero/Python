from tkinter import *

from click import command

food = ["pizza", "hamburger", "hotdogs"]
def order():
    print(f"You Ordered {food[x.get()]} !")

w = Tk()
# w.config(background="#000000")

x = IntVar()
pizza = PhotoImage(file="/media/zero/Software/__/Python/Pygame/64pix_bullet/png/013-nuclear.png")
hamburger = PhotoImage(file="/media/zero/Software/__/Python/Pygame/64pix_bullet/png/019-nuclear-bomb-1.png")
hotdogs = PhotoImage(file="/media/zero/Software/__/Python/Pygame/64pix_bullet/png/036-nuclear-energy.png")
photos = [pizza,hamburger,hotdogs]

for i in range(len(food)):
    radiobutton = Radiobutton(
        w,
        text=food[i],
        variable=x,
        value=i,
        padx=25,
        # pady=10,
        font=("Arial", 20),
        # fg="#00FF00",
        # bg="black",
        # activebackground="black",
        # activeforeground="#00FF00",
        image=photos[i],
        compound=LEFT,
        # indicatoron=0,
        width= 350,
        command=order
    )
    radiobutton.pack(anchor="w")

w.mainloop()
