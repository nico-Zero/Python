from turtle import Turtle


class Player(Turtle):
    def __init__(
        self,
        shape="turtle",
        color="black",
        location=(0, -350),
    ):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.penup()
        self.setheading(90)
        self.goto(*location)
        self.location = location

    def up(self, motion=10):
        self.forward(motion)

    def down(self, motion=10):
        self.backward(motion)

    def control(self, s):
        s.screen.onkey(fun=self.up, key="Up")
        s.screen.onkey(fun=self.down, key="Down")

    def is_level_up(self):
        if self.ycor() > abs(self.location[1]):
            return True
        return False

    def reset(self):
        self.goto(*self.location)
