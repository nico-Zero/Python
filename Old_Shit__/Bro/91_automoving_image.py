from tkinter import *
import time

WIDTH = 600
HEIGHT = 500
speedx,speedy = 2,2
run = True

def write(event):
    global run
    if run:
        run = False
    else:
        run = True
    move()

def move():
    global speedx, speedy
    while run:
        if run:
            coordinates = c.coords(n)
            # print(coordinates)
            if coordinates[0] > 536 or coordinates[0] < 0 :
                speedx = speedx*(-1)
            elif coordinates[1] > 436 or coordinates[1] < 0 :
                speedy = speedy*(-1)
            w.bind("<space>",write)
            c.move(n,speedx,speedy)
            w.update()
            time.sleep(0.01)
    
w= Tk()

nucler = PhotoImage(file="/media/zero/Software/__/Python/Pygame/64pix_bullet/png/018-nuclear-1.png")

c = Canvas(width=WIDTH,height=HEIGHT)
c.pack()
n =c.create_image(268,218,image= nucler,anchor=NW)
move()

w.mainloop()
