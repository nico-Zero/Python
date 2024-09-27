from turtle import Turtle
from random import randint, choice


COLORS = [
    "black",
    "green",
    "red",
    "yellow",
    "orange",
    "pink",
    "blue",
    "purple",
    "brown",
]


class Cars:
    def __init__(self, length=3, density=8, motion=4):
        self.list_of_cars = []
        self.helper = 1
        self.length = length
        self.density = density
        self.motion = motion

    def create_car(self):
        if self.helper % self.density:
            self.helper += 1
            pass
        else:
            self.helper += 1

            car = Turtle()
            car.color(choice(COLORS))
            car.setheading(180)
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=self.length)
            car.penup()
            car.goto(520, randint(-290, 290))
            self.list_of_cars.append(car)

    def move(self):
        for car in self.list_of_cars:
            car.forward(self.motion)

    def check_collision(self, human):
        for car in self.list_of_cars:
            if (car.ycor() - 20) < human.ycor() < (car.ycor() + 20):
                if (
                    car.xcor() - (self.length * 10)
                    < human.xcor()
                    < car.xcor() + (self.length * 10)
                ):
                    return True
        return False

    def increase_density(self, increase=2):
        if not self.density <= 2:
            self.density -= increase

    def speed_up(self, speed):
        self.motion += speed
