# from tkinter import *

# speed = 10

# def move_up(event):
#     l.place(x=l.winfo_x(),y=l.winfo_y()-speed)
# def move_down(event):
#     l.place(x=l.winfo_x(),y=l.winfo_y()+speed)
# def move_left(event):
#     l.place(x=l.winfo_x()-speed,y=l.winfo_y())
# def move_right(event):
#     l.place(x=l.winfo_x()+speed,y=l.winfo_y())

# w = Tk()

# w.geometry("500x500")

# w.bind("<w>",move_up)
# w.bind("<s>",move_down)
# w.bind("<a>",move_left)
# w.bind("<d>",move_right)
# w.bind("<Up>",move_up)
# w.bind("<Down>",move_down)
# w.bind("<Left>",move_left)
# w.bind("<Right>",move_right)

# bullet = PhotoImage(file="/media/zero/Software/__/Python/Pygame/64pix_bullet/png/004-bullet-3.png")

# l = Label(w,image=bullet)
# # l.bind("<>",T)
# # l.bind("<>",motion)
# l.place(x=0,y=0)

# w.mainloop()

######################################################################
######################################################################

from tkinter import *

speed = 10

def move_up(event):
    c.move(mYimage,0,-5)
def move_down(event):
    c.move(mYimage,0,5)
def move_left(event):
    c.move(mYimage,-5,0)
def move_right(event):
    c.move(mYimage,5,0)

w = Tk()

w.bind("<w>",move_up)
w.bind("<s>",move_down)
w.bind("<a>",move_left)
w.bind("<d>",move_right)
w.bind("<Up>",move_up)
w.bind("<Down>",move_down)
w.bind("<Left>",move_left)
w.bind("<Right>",move_right)

c = Canvas(width=500,height=500)
c.pack()
bomb = PhotoImage(file="/media/zero/Software/__/Python/Pygame/64pix_bullet/png/039-bomb.png")
mYimage = c.create_image(0,0,image=bomb,anchor=NW)

w.mainloop()
