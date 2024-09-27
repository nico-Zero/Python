from pandas import read_csv, DataFrame
from turtle import Turtle, Screen

# Writer And Background.
t = Turtle()
writer = Turtle()
writer.penup()
writer.hideturtle()

# Screen
screen = Screen()
screen.setup(width=1093, height=740)
screen.title("U.S State Game")

# Image section.
image = "blank_state_150.gif"
screen.addshape(image)
t.shape(image)

# Data section.
state_file = "50_states.csv"
usa_state = read_csv(state_file)

# Listing Section
state_name = usa_state.state.to_list()
x = [i + i * (1 / 2) for i in usa_state.x.to_list()]
y = [i + i * (1 / 2) for i in usa_state.y.to_list()]

print(*state_name, sep="\n")

# scores
score = 0
s_wri = Turtle()
s_wri.penup()
s_wri.hideturtle()


def update_score():
    s_wri.clear()
    s_wri.goto(-490, 320)
    s_wri.write(f"{score}/50", align="center", font=("Courier", 25, "normal"))

    return f"{score}/50"


while 1 if 50 - len(state_name) < 50 else print("Win!!"):
    # Updating score

    # Taking input from the player
    guess = screen.textinput(update_score(), "Enter a State Name...").title()

    # Checking if the state name is write
    if guess == "Exit" or guess == "E":
        break
    elif guess in state_name:
        i = state_name.index(guess)
        writer.goto(x[i], y[i])
        writer.write(guess, align="center", font=("Courier", 12, "normal"))

        # removing the state name from the variables
        state_name.remove(guess)
        x.remove(x[i])
        y.remove(y[i])

        # Updating the score
        score += 1

left_state_name = DataFrame({"state": state_name})
left_state_name.to_csv("learn_states.csv")
