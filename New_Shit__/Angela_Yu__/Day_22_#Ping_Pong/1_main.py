from display import Display
from turtle import Turtle
from time import sleep
from ball import Ball
from bar import Bar


WIDTH = 1000
HEIGHT = 800
DISTANCE_FROM_WALL = 30
SIDES = ["left", "right", "top", "bottom"]
switch = True
b_1_score = 0
b_2_score = 0
score_limit = int(input("Enter goal:- "))
speed = 0.03
winner_l = 150

monitor = Display()
b_1 = Bar(
    command="left",
    screen=monitor.screen,
    location=(-((WIDTH / 2) - DISTANCE_FROM_WALL), 0),
    movement=5,
)
b_2 = Bar(
    command="right",
    screen=monitor.screen,
    location=((WIDTH / 2) - DISTANCE_FROM_WALL, 0),
    movement=5,
)
ball = Ball(location_reset=True)

score = Turtle()
score.color("white")
score.hideturtle()
score.penup()
score.goto(0, (HEIGHT / 2) - 100)

f = ("Courier", 80, "normal")


def score_board():
    score.clear()
    score.write(f"{b_1_score}   {b_2_score}", align="center", font=f)


def speed_up():
    global speed
    if speed > 0.001:
        speed -= 0.001


def winner(location):
    score.goto(location, 0)
    score.write("Winner", align="center", font=("Courier", 40, "normal"))


while True:
    if (side := ball.motion()) in SIDES:
        if side == "left":
            b_2_score += 1
        elif side == "right":
            b_1_score += 1
        speed_up()

    if b_1.check_collision(ball, "ball.xcor() < -450"):
        ball.x *= -1
        speed_up()
    elif b_2.check_collision(ball, "ball.xcor() > 450"):
        ball.x *= -1
        speed_up()

    monitor.screen.update()

    score_board()
    sleep(speed)
    if b_1_score >= score_limit or b_2_score >= score_limit:
        break

if b_1_score > b_2_score:
    winner(-winner_l)
elif b_1_score < b_2_score:
    winner(winner_l)
else:
    winner(-winner_l)
    winner(winner_l)

# print("Game Over!")

monitor.screen.exitonclick()
