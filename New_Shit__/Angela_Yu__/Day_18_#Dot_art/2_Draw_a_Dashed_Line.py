from turtle import Screen, Turtle
from faker import Faker

tim = Turtle()
f = Faker()

angle = 15
i = 0

for _ in range(2, angle):
    while 1:
        tim.right(i)
        tim.forward(100)
        if round(tim.position()[0]) == 100 and round(tim.position()[1]) == 0:
            tim.color(f.color_name())
            i = 360 / (_ + 1)
            break

screen = Screen()
screen.exitonclick()
