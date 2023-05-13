from turtle import Turtle


class Bar(Turtle):
    def __init__(
        self,
        command=None,
        screen=None,
        color="white",
        location=(0, 0),
        length=7,
        movement=20,
        side="horizontal",
    ):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.goto(location)
        if side == "horizontal":
            self.shapesize(stretch_wid=length, stretch_len=1)
        elif side == "vertical":
            self.shapesize(stretch_wid=1, stretch_len=length)
        self.movement = movement
        self.control(command, screen)

    def check(self):
        if -330 > self.ycor():
            self.sety(-330)
            return 1
        elif self.ycor() > 330:
            self.sety(330)
            return 1
        return 0

    def up(self):
        if self.check():
            return 0
        self.goto(self.xcor(), self.ycor() + self.movement)

    def down(self):
        if self.check():
            return 0
        self.goto(self.xcor(), self.ycor() - self.movement)

    def control(self, command, screen):
        if command == "left":
            screen.onkey(fun=self.up, key="w")
            screen.onkey(fun=self.down, key="s")
        elif command == "right":
            screen.onkey(fun=self.up, key="Up")
            screen.onkey(fun=self.down, key="Down")

    def check_collision(self, ball, con):
        y_t = self.ycor() + 70
        y_b = self.ycor() - 70
        if self.distance(ball) < 70 and eval(con) and y_t > ball.ycor() > y_b:
            return True
