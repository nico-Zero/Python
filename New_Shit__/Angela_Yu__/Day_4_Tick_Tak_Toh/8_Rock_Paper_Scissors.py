from random import randint
from os import system
rock = """    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
option = [rock,paper,scissors]
system("cls")

while 1:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    try:
        print(option[choice])

        num = randint(0,2)
        print(f"Computer choice :{option[num]}")

        if num == choice:
            print("Drow...")
        elif choice == 0 and num == 2:
            print("You win...")
        elif not choice == 0 and num == 2:
            print("You lose...")
        elif num > choice:
            print("You lose...")
        else:
            print("You win...")
    except:
        print("Error !")
    qu = input("Would you like to play again? Y/N ? ").lower()
    if qu == "n":
        break
    system("cls")