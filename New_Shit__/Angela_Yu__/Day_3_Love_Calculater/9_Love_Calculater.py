import re

name1 = input("What is your name ?\n").lower()
name2 = input("What is your lover's name ?\n").lower()

true = re.findall(r"[true]", name1 + name2)
love = re.findall(r"[love]", name1 + name2)
score = int(str(len(true)) + str(len(love)))

if 10 > score or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")