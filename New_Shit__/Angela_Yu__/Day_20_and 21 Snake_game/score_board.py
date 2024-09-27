from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 420)
        self.write_in_screen()

    def write_in_screen(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self, c="white"):
        self.color(c)
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=("Arial", 80, "normal"))
