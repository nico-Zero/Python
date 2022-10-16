from turtle import Turtle, Screen
from random import choice
from color import color_list

t = Turtle()
t.hideturtle()
t.pensize(8)
t.speed(0)

angle = [90, 180, -90]

for _ in range(1000):
    t.color(choice(color_list))
    t.forward(20)
    t.left(choice(angle))

screen = Screen()
screen.exitonclick()
