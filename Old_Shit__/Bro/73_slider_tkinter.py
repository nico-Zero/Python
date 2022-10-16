from tkinter import *


def submit():
    print(f"The temperature is: {scale.get()}C")


w = Tk()

photo1 = PhotoImage(file="/media/zero/Software/__/Python/Pygame/64pix_bullet/png/021-nuclear-bomb-3.png")
Label(w,image=photo1).pack()

scale = Scale(
    w,
    from_= (f:=100),
    to=(t:=-f),
    length=600,
    orient=VERTICAL,
    font=("Arial", 15),
    tickinterval=10,
    showvalue=0,
    resolution=5,
    troughcolor="#696969",
    fg="#980d0e",
    bg="#000000",

)
scale.set(((f-t)//2)+t)
scale.pack()
photo2 = PhotoImage(file="/media/zero/Software/__/Python/Pygame/64pix_bullet/png/015-atom-1.png")
Label(w,image=photo2).pack()

button = Button(w, text="submit", command=submit)
button.pack()

w.mainloop()
