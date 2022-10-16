from tkinter import *


def print_value():
    print(x.get())


def display():
    if x.get() == 1:
        print("Yes I agree!")
    else:
        print("No I disagree :(")


w = Tk()

x = IntVar()
photo = PhotoImage(
    file="/media/zero/Software/__/Python/Pygame/64pix_bullet/png/038-biohazard.png"
)

check_button = Checkbutton(
    w,
    text="I agree to somwthing.",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display,
    font=("Arial", 20),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    padx=25,
    pady=10,
    image=photo,
    compound=LEFT
)
p_button = Button(w, text="Enter", command=print_value)

check_button.pack()
p_button.pack()

w.mainloop()
