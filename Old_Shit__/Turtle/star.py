from turtle import *
import turtle
import math
import random

t =  Turtle()
t.speed(11)
t.getscreen().bgcolor('#b30202')

def star(x):
    if x <= 10:
        return
    else:
        for i in range(5):
            t.forward(x)
            star(x/3)
            t.left(216)
star(200)


turtle.done()