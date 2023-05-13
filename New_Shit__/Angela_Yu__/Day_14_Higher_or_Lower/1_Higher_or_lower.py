from random import choice
from faker import Faker
from os import system
import logo

# Important variables
f = Faker()
score = 0


# Function to gestate random number
def choc():
    return choice(range(0, 100000000, 10000))


def values():
    return [f.name().title(), f.job().title(), f.country().title()]


system("cls")

# Creating values for compression.
a_value = values()
b_value = values()
a = choc()
b = choc()

# The main loop
while 1:

    # The second main loop
    while 1:

        # Printing the logo
        print(logo.logo)

        # Printing the score
        print("Score:", ("❤️" * score) or 0)

        # Below printing other stuffs
        print(f"Compare A: {a_value[0]}, a {a_value[1]}, from {a_value[2]}.")
        print(logo.vs)
        print(f"Against B: {b_value[0]}, a {b_value[1]}, from {b_value[2]}.")

        # Switching the values
        if a < b:
            a_value = b_value
        else:
            pass

        # Assigning new values
        b_value = values()

        # Taking the input of the user
        re = input("Who has more followers? Type 'A' or 'B' : ").lower()

        # Checking if the user is correct or not.
        system("cls")
        if re == "a":
            if a > b:
                # Updating values
                b = choc()
                score += 1
            else:
                print("Your Final :", score)
                break
        elif re == "b":
            if b > a:
                # Updating values
                a, b = b, choc()
                score += 1
            else:
                print("Your Final :", score)
                break
        else:
            print("Wrong Input")
            print("Your final :", score)
            break

    # Asking if user would like to play the game again.
    score = 0
    if input("Would you like to play again? Y/N: ").lower() == "y":
        system("cls")
        pass
    else:
        system("cls")
        break
