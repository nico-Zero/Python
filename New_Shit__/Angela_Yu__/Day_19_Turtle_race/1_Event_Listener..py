from turtle import Screen, Turtle

t = Turtle()
t.speed(0)
screen = Screen()
motion = int(input("Enter a number of motion:- "))


def move_forward():
    t.forward(motion)


def move_backward():
    t.backward(motion)


def move_left():
    t.left(10)


def move_right():
    t.right(10)


def clear():
    t.home()
    t.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
