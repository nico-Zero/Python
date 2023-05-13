from random import choice
from os import system

logo = """
    _______  ________  ________  ________  ________      _______        _______  ________  ________  ________  ________  ________ 
  ╱╱       ╲╱    ╱   ╲╱        ╲╱        ╲╱        ╲    ╱       ╲╲    ╱╱   ╱   ╲╱    ╱   ╲╱        ╲╱       ╱ ╱        ╲╱        ╲
 ╱╱      __╱         ╱         ╱        _╱        _╱   ╱        ╱╱   ╱╱        ╱         ╱         ╱        ╲╱         ╱         ╱
╱       ╱ ╱         ╱        _╱-        ╱-        ╱   ╱         ╱   ╱         ╱         ╱         ╱         ╱        _╱        _╱ 
╲________╱╲________╱╲________╱╲________╱╲________╱    ╲___╱____╱    ╲__╱_____╱╲________╱╲__╱__╱__╱╲________╱╲________╱╲____╱___╱  

"""

system("clear")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
e_h = input("Choose a difficulty. Type 'easy' or 'hard': ")
system("clear")
attmpt = 10 if e_h == "easy" else 5
random_number = choice(range(0, 100, 10)) if e_h == "easy" else choice(range(1, 100))


def guess_check():
    global attmpt
    if guess == random_number:
        print(f"You got it. It's {random_number}.")
        return True
    else:
        attmpt -= 1
        if guess - random_number >= 20:
            print("Too high.")
        elif guess - random_number >= 10:
            print("High.")
        elif -10 < guess - random_number < 10:
            print("Your close.")
        elif guess - random_number <= -20:
            print("Too low.")
        elif guess - random_number <= -10:
            print("Low.")
        print("Guess again.")
        return False


while 1:
    print(logo)
    print(f"You have {attmpt} attmpts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    system("clear")
    if guess_check():
        break
    elif attmpt == 0:
        system("clear")
        print("You Loss.")
        break
