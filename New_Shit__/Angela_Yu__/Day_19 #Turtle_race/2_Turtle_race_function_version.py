from turtle import Screen, Turtle
from functools import reduce
from random import randint

screen = Screen()
screen.setup(width=1000, height=1000)
list_of_color = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "brown",
    "orange",
    "pink",
    "gray",
]
list_of_turtle = [
    Turtle(shape="turtle", visible=False) for _ in range(len(list_of_color))
]

title = "Make Choice..."
prompt_1 = reduce(lambda x, y: x + "," + y, list_of_color)
prompt_2 = "\nWhich color do you think will win?"


user_choice = screen.textinput(title, prompt_1 + prompt_2)

for i in list_of_turtle:
    i.penup()


def change_speed(turtle, speed):
    for i in turtle:
        i.speed(speed)


def change_size(turtle, size):
    for i in turtle:
        i.shapesize(size, size, size)


def color_them(color_list, turtle):
    for i, j in zip(color_list, turtle):
        j.color(i)
        j.showturtle()


def sety(turtle, dis):
    for i, j in zip(turtle, range(-200, (len(turtle) * dis) + 1, dis)):
        i.goto(-460, j)


def random_move(turtle, move):
    for i in turtle:
        i.forward(randint(1, move))
        if not check_position(turtle):
            return True
    return False


def check_position(turtle):
    global x
    for i in turtle:
        if i.xcor() > 460:
            x = turtle.index(i)
            print(f"{list_of_color[x]} win...")
            return False
        else:
            continue
    return True


change_speed(list_of_turtle, 0)
sety(list_of_turtle, 40)
change_speed(list_of_turtle, 2)
change_size(list_of_turtle, 2)
color_them(list_of_color, list_of_turtle)

while 1:
    if random_move(list_of_turtle, 20):
        break

if list_of_color[x] == user_choice:
    print("You'r gauss was right!")
else:
    print("You gauss were wrong!")

screen.exitonclick()
