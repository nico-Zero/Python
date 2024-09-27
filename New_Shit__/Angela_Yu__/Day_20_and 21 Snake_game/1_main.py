from snake import Snake, Turtle
from food import Food
from score_board import Score_board
from turtle import Screen


screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)

score_board = Score_board()
f_1 = Food(Turtle("circle"))
s_1 = Snake(snake_count=3, shape="square", speed=0.08)


def check_bound(turtle):
    for i in turtle:
        if i.xcor() > 430 or i.xcor() < -430:
            return True
        elif i.ycor() > 430 or i.ycor() < -430:
            return True
    return False


def game_over():
    if check_bound(s_1.snake) or s_1.check_tail():
        return False
    return True


while game_over():
    s_1.motion()
    screen.update()
    s_1.speed_up()
    if f_1.check_hunger(s_1.snake):
        s_1.add_snake()
        score_board.write_in_screen()
    s_1.key(screen)

score_board.game_over()

screen.exitonclick()
