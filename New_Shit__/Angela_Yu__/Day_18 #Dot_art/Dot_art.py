from turtle import Screen, Turtle, colormode
from color import colors
from random import choice

screen = Screen()
screen.screensize(800, 800)

t = Turtle()
colormode(255)

t.hideturtle()
t.penup()
t.speed(0)
x = -460
y = 390

color_list = colors(30)
x_change = 20
y_change = 20

while 1:
    if y < -390:
        break
    t.goto(x, y)
    t.dot(20, choice(color_list))
    x += x_change
    if x > 460:
        x = -460
        y -= y_change

screen.exitonclick()
