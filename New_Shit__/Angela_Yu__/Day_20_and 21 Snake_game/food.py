from random import randint


class Food:
    def __init__(self, food_turtle) -> None:
        self.food = food_turtle
        self.food.color("red")
        self.food.penup()
        self.random_food()

    def random_food(self):
        self.food.hideturtle()
        self.food.goto(randint(-410, 410), randint(-410, 410))
        self.food.showturtle()

    def check_hunger(self, snake):
        if snake[0].distance(self.food.pos()) < 22:
            self.random_food()
            return 1
