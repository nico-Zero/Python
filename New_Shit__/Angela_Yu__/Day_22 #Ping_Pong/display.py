from turtle import Screen, Turtle


class Display:
    def __init__(self, w=1000, h=800, color="black", location=800):
        self.screen = Screen()
        self.screen.title("Pong Game")
        self.screen.setup(width=w, height=h)
        self.screen.bgcolor(color)
        self.screen.tracer(0)
        self.screen.listen()
        self.mid_line(location=location)

    def mid_line(self, location):
        line = Turtle()
        line.color("white")
        line.hideturtle()
        line.penup()
        line.goto(0, location / 2)
        line.setheading(270)
        line.width(5)
        while 1:
            if line.ycor() > -(location / 2):
                line.pendown()
                line.forward(10)
                line.penup()
                line.forward(10)
            else:
                break
