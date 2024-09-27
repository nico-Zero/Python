from turtle import *
import turtle
import math
import random

t  = Turtle()
t.color("red","yellow")
t.speed(11)

t.begin_fill()
for i in range(20000):
    t.forward(10)
    t.left(math.sin(i/10)*25)
    t.left(20)

t.end_fill()
# turtle.done()
print(dir(math))