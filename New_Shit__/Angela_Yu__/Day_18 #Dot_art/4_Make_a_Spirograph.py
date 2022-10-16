from turtle import Screen, Turtle
from random import choice
from color import color_list

radius = int(input("Enter the radius of the circle:- "))
i = int(input("Enter the level of density:- "))

t = Turtle()
t.hideturtle()
t.speed(0)

for _ in range(round(360/i)):
    t.circle(radius)
    t.pencolor(choice(color_list))
    t.left(i)

screen = Screen()
screen.exitonclick()
