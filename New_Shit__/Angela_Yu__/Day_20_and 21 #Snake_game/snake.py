from turtle import Turtle
from time import sleep


class Snake:
    def __init__(self, snake_count=3, shape="square", speed=0.07):
        self.speed = speed
        self.shape = shape
        self.snake_count = snake_count
        self.snake = [Turtle(shape=self.shape) for _ in range(snake_count)]
        self.head = self.snake[0]

        after = -((20 * (snake_count - 3)) + 1)
        for i, j in zip(self.snake, range(40, after, -20)):
            i.penup()
            i.color("white")
            i.forward(j)

    def motion(self):
        x, y, k = self.head.xcor(), self.head.ycor(), None
        k
        self.head.forward(20)
        for i in self.snake[1:]:
            x, y, k = i.xcor(), i.ycor(), i.goto(x, y)

    def add_snake(self):
        new_snake = Turtle(shape=self.shape)
        new_snake.penup()
        new_snake.color("white")
        self.snake.append(new_snake)

    def check_tail(self):
        list_of_pos = [self.head.distance(i) for i in self.snake[1:]]

        if min(list_of_pos) <= 10:
            return True
        return False

    def speed_up(self):
        sleep(self.speed)

    def turn_up(self):
        if not (self.head.heading() == 270):
            self.head.setheading(90)

    def turn_down(self):
        if not (self.head.heading() == 90):
            self.head.setheading(270)

    def turn_left(self):
        if not (self.head.heading() == 0):
            self.head.setheading(180)

    def turn_right(self):
        if not (self.head.heading() == 180):
            self.snake[0].setheading(0)

    def key(self, screen):
        # Left Control
        screen.onkey(key="w", fun=self.turn_up)
        screen.onkey(key="s", fun=self.turn_down)
        screen.onkey(key="a", fun=self.turn_left)
        screen.onkey(key="d", fun=self.turn_right)

        # Right Control
        screen.onkey(key="Up", fun=self.turn_up)
        screen.onkey(key="Down", fun=self.turn_down)
        screen.onkey(key="Left", fun=self.turn_left)
        screen.onkey(key="Right", fun=self.turn_right)
