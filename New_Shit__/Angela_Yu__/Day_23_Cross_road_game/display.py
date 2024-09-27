from turtle import Screen, Turtle
from time import sleep


class Display:
    def __init__(
        self,
        sep=0.08,
        w=1000,
        h=800,
        color="white",
        listen=True,
        font=("Courier", 40, "normal"),
        level=1,
    ):
        self.screen = Screen()
        self.screen.title("Cross Rode")
        self.screen.setup(width=w, height=h)
        self.screen.bgcolor(color)
        self.screen.tracer(0)
        if listen:
            self.screen.listen()
        self.font = font
        self.sep = sep
        self.level = level

        #  Score Board
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(-370, 340)
        self.show_level()

    def speed(self):
        sleep(self.sep)

    def show_level(self):
        label = f"Level-{self.level}"
        self.turtle.write(label, align="center", font=self.font)

    def level_up(self):
        self.level += 1
        self.turtle.clear()
        self.show_level()

    def game_over(self):
        self.turtle.goto(0, 0)
        f = ("Courier", 70, "normal")
        self.turtle.write("Game Over!", align="center", font=f)
