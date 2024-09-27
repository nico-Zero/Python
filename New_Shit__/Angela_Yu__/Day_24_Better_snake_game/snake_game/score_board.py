from turtle import Turtle


ALIGN = "center"
FONT = ("Courier", 20, "normal")
FILE = (
    "high_score.txt"
)


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(
            FILE,
            "r",
        ) as f:
            self.high_score = int(f.read())
        self.copy_of_high_score = self.high_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 420)
        self.write_in_screen()

    def write_in_screen(self):
        self.clear()
        self.write(
            f"Score: {self.score}, Highest Score: {self.high_score}",
            align=ALIGN,
            font=FONT,
        )

    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        if self.copy_of_high_score < self.high_score:
            with open(
                FILE,
                "w",
            ) as f:
                f.write(str(self.high_score))

        self.write_in_screen()

    def game_over(self, c="white"):
        self.color(c)
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=("Courier", 80, "normal"))
