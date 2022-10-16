import random
from os import system

choices = ["rock", "paper", "scissors"]

while 1:
    system("clear")
    print("\n#######################################")
    print("#######################################")
    player = input(
        """
Enter Rock or
      paper or
      scissors   
player   :- """
    ).lower()

    if player == "q" or player == "Q":
        break

    computer = random.choice(choices)
    print("computer :-", computer)
    if player == computer:
        print("\nDraw...")
    elif player == choices[0] and computer == choices[1]:
        print("\nComputer Win...")
    elif player == choices[1] and computer == choices[2]:
        print("\nComputer Win...")
    elif player == choices[2] and computer == choices[0]:
        print("\nComputer Win...")
    elif player == choices[1] and computer == choices[0]:
        print("\nPlayer Win...")
    elif player == choices[2] and computer == choices[1]:
        print("\nPlayer Win...")
    elif player == choices[0] and computer == choices[2]:
        print("\nPlayer Win...")
    else:
        print("\nInvalid input...):):):______")

    play_again = input("\nPlay again? (y/n):- ").lower()
    if play_again == "yes":
        continue
    else:
        break
