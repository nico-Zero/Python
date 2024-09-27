from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(
        self,
        color="white",
        location=(randint(-300, 300), randint(-400, 400)),
        location_reset=False
    ):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color(color)
        self.goto(location)
        self.location_reset = location_reset
        self.x = 10
        self.y = 10

    def motion(self, location_reset=False):
        x, y = self.position()
        if y > 380 or y < -380:
            self.y *= -1
            self.goto(x + self.x, y + self.y)
            return 0
        elif x > 480 or x < -480:
            self.x *= -1
            self.goto(x + self.x, y + self.y)
            if self.location_reset or location_reset:
                self.goto(0, 0)
            if x < -480:
                return "left"
            else:
                return "right"
        self.goto(x + self.x, y + self.y)
        return 0
