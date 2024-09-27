from multiprocessing import Lock
import turtle
import time

# Score
a = 0
b = 0

# Player mode choices
while True:
    i = int(input("Enter Player mode 1 or 2:- "))
    if i == 1 or i == 2:
        break

if i == 2:
    j = False
    i = False
else:
    j = True
    i = True

# Creating screen
w = turtle.Screen()
w.title("Pong by Zero")
w.bgcolor("black")
w.setup(width=800, height=600)
w.tracer(0)


# Paddle A
p_a = turtle.Turtle()
p_a.speed(0)
p_a.shape("square")
p_a.color("white")
p_a.shapesize(stretch_wid=5, stretch_len=1)
p_a.penup()
p_a.goto(-350, 0)

# Paddle B

p_b = turtle.Turtle()
p_b.speed(0)
p_b.shape("square")
p_b.color("white")
p_b.shapesize(stretch_wid=5, stretch_len=1)
p_b.penup()
p_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize()
ball.penup()
ball.goto(0, 0)

ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    f"Player A: {a}  Player B: {b}", align="center", font=("Courier", 24, "normal")
)

# Movement Function of paddle
def move_a_up():
    y = p_a.ycor()
    if p_a.ycor() < 250:
        y += 5
        p_a.sety(y)


def move_a_down():
    y = p_a.ycor()
    if p_a.ycor() > -250:
        y -= 5
        p_a.sety(y)


if j == False:

    def move_b_up():
        y = p_b.ycor()
        if p_b.ycor() < 250:
            y += 5
            p_b.sety(y)

    def move_b_down():
        y = p_b.ycor()
        if p_b.ycor() > -250:
            y -= 5
            p_b.sety(y)


def exit():
    turtle.bye()


# Call
w.listen()
if j:
    w.onkeypress(move_a_up, "Up")
    w.onkeypress(move_a_down, "Down")
elif j == False:
    w.onkeypress(move_a_up, "w")
    w.onkeypress(move_a_down, "s")
    w.onkeypress(move_b_up, "Up")
    w.onkeypress(move_b_down, "Down")

w.onkeypress(exit, "c")

while True:
    w.update()
    global x
    x = 0.01
    time.sleep(x)
    with Lock():
        # Single Player
        if j:
            if ball.ycor() > 250:
                p_b.sety(250)
            elif ball.ycor() < -250:
                p_b.sety(-250)
            else:
                p_b.sety(ball.ycor())

        # Ball movement function
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # Border checking
        # Top
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        # Buttom
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        # Left
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            b += 1
            pen.clear()
            pen.write(
                f"Player A: {a}  Player B: {b}",
                align="center",
                font=("Courier", 24, "normal"),
            )
            if i:
                j = True
        # Right
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            a += 1
            pen.clear()
            pen.write(
                f"Player A: {a}  Player B: {b}",
                align="center",
                font=("Courier", 24, "normal"),
            )
            if i:
                j = False
        # Bounce
        if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < p_b.ycor() + 50 and ball.ycor() > p_b.ycor() - 50
        ):
            ball.setx(340)
            ball.dx *= -1
            if i:
                j = False
                p_b.sety(0)
            # x -= 0.002

        if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < p_a.ycor() + 50 and ball.ycor() > p_a.ycor() - 50
        ):
            ball.setx(-340)
            ball.dx *= -1
            if i:
                j = True
            # x -= 0.002
