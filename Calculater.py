from tkinter import *
import re

M_O = ["+", "-", "*", "/", "^"]
value = []
con = False


# Moniter operation
def button_press(x):
    no_value()
    global con
    if con:
        moniter_2.delete(0, END)
    moniter_1.insert(END, x)
    Core()
    con = False


def Clear():
    moniter_1.delete(0, END)
    moniter_2.delete(0, END)
    value.clear()


def Core():
    moniter_2.delete(0, END)
    try:
        x = moniter_1.get().replace("^", "**")
        if (moniter_1.get())[-1] in M_O and (moniter_1.get())[-2] == ".":
            moniter_2.insert(END, f"={eval(x[:-2])}")
        elif (moniter_1.get())[-1] in M_O:
            moniter_2.insert(END, f"={eval(x[:-1])}")
        else:
            moniter_2.insert(END, f"={eval(x)}")
    except (SyntaxError, IndexError):
        pass


def Ans():
    if (moniter_1.get()) != "":
        global con
        Core()
        value.clear()
        moniter_1.delete(0, END)
        con = True


def Delete():
    global value
    no_value()
    if len(value) == 1:
        value.clear()
    try:
        if (moniter_1.get())[-2] == ".":
            moniter_1.delete(len(moniter_1.get()) - 2, END)
        else:
            moniter_1.delete(len(moniter_1.get()) - 1, END)
    except IndexError:
        moniter_1.delete(0, END)
        value.clear()
    Core()


def Dot():
    no_value()
    dot_count = (moniter_1.get()).count(".")
    if (value[-1]).count(".") == 0:
        if dot_count <= len(value):
            moniter_1.insert(END, ".")


# Some importent Functions
def no_value():
    global value
    value = re.split(r"\+|-|\*|/|\^", moniter_1.get())


# Mathematical operation
def Math_operator(x):
    try:
        if not (moniter_1.get())[-1] in M_O:
            no_value()
            moniter_1.insert(END, x)
    except IndexError:
        pass


def Per():
    if not moniter_1.get() == "":
        x = moniter_1.get()
        y = (moniter_2.get())[1:]
        v = len(value) <= 1
        Clear()
        if v:
            moniter_1.insert(END, eval(f"{x}/100"))
        else:
            moniter_1.insert(END, eval(f"{y}/100"))


w = Tk()
w.title("Calculater Program")
# w.geometry("500x500")

moniter_1 = Entry(w, width=50, justify=RIGHT)
moniter_1.grid(columnspan=4, row=0, pady=0)

moniter_2 = Entry(w, width=50, justify=RIGHT)
moniter_2.grid(columnspan=4, row=1, pady=0)

button_0 = Button(w, text="0", padx=50, pady=20, command=lambda: button_press(0))
button_1 = Button(w, text="1", padx=50, pady=20, command=lambda: button_press(1))
button_2 = Button(w, text="2", padx=50, pady=20, command=lambda: button_press(2))
button_3 = Button(w, text="3", padx=50, pady=20, command=lambda: button_press(3))
button_4 = Button(w, text="4", padx=50, pady=20, command=lambda: button_press(4))
button_5 = Button(w, text="5", padx=50, pady=20, command=lambda: button_press(5))
button_6 = Button(w, text="6", padx=50, pady=20, command=lambda: button_press(6))
button_7 = Button(w, text="7", padx=50, pady=20, command=lambda: button_press(7))
button_8 = Button(w, text="8", padx=50, pady=20, command=lambda: button_press(8))
button_9 = Button(w, text="9", padx=50, pady=20, command=lambda: button_press(9))
button_dot = Button(w, text=".", padx=52, pady=20, command=Dot)

button_add = Button(w, text="+", padx=49, pady=20, command=lambda: Math_operator("+"))
button_sub = Button(w, text="-", padx=51, pady=20, command=lambda: Math_operator("-"))
button_mul = Button(w, text="*", padx=51, pady=20, command=lambda: Math_operator("*"))
button_div = Button(w, text="/", padx=51, pady=20, command=lambda: Math_operator("/"))
button_pow = Button(w, text="^", padx=49, pady=20, command=lambda: Math_operator("^"))
button_per = Button(w, text="%", padx=48, pady=20, command=Per)

button_delete = Button(w, text="<-", padx=46, pady=20, command=Delete)
button_clear = Button(w, text="Clear", padx=37, pady=20, command=Clear)
button_ans = Button(w, text="=", padx=49, pady=20, command=Ans)

# Griding the button on the screen
button_clear.grid(row=2, column=0)
button_delete.grid(row=2, column=1)
button_per.grid(row=2, column=2)
button_div.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_sub.grid(row=4, column=3)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_add.grid(row=5, column=3)

button_pow.grid(row=6, column=1)
button_0.grid(row=6, column=0)
button_dot.grid(row=6, column=2)
button_ans.grid(row=6, column=3)

w.mainloop()
# 10:18:31
