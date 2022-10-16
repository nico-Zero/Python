from tkinter import *
from Ball import *

def stop(event):
    global run
    if run:
        run = False
    else:
        run = True
    move_all()

def move_all():
    while run:
        if run:
            Vally_ball.move()
            Base_ball.move()
            Nova_ball.move()
            Golf_ball.move()
            w.bind("<space>", stop)
        else:
            return

WIDTH = 600
HEIGHT = 500
run = True

w = Tk()

c = Canvas(width=WIDTH, height=HEIGHT)
c.pack()

Vally_ball = Ball(w, c, 300, 300, 400, 3, 3, "#ff7600", WIDTH, HEIGHT)
Base_ball = Ball(w, c, 200, 200, 350, 5, 5, "#de96d7", WIDTH, HEIGHT)
Nova_ball = Ball(w, c, 50, 50, 250, 2, 2, "#ffbb00", WIDTH, HEIGHT)
Golf_ball = Ball(w, c, 0, 0, 50, 4, 4, "#00ff68", WIDTH, HEIGHT)

move_all()

w.mainloop()
