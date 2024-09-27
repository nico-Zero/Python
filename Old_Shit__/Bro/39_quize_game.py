from os import system
from time import sleep

questions = {
    "Who created Python ?": "A",
    "What year was Python created ?": "B",
    "Python is tributed to which comedy group ?": "C",
    "Is the Earth round ?": "A",
}

option = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Something", "D. What's Earth?"],
]

def new_game():
    global value,sl
    score = 0
    value = []
    sl = 0.2
    for i, j in zip(questions.keys(), range(len(questions))):
        x = j + 1
        sleep(sl)
        print(f"{x}.", i, end="\n\n")
        for l in option[j]:
            sleep(sl)
            print(l)
        sleep(sl)
        value.append((input("\nEnter your choice:- ")).upper())
        if value[j] == "Q":
            return "Q"
        score += check(j)
        print("#" * 30, "\n")
    return score

def check(i):
    if value[i] == (list(questions.values()))[i]:
        sleep(sl)
        print("CORRECT")
        return 1
    else:
        sleep(sl)
        print("WRONG")
        return 0

def display_score(score):
    if score == "Q":
        return score
    sleep(sl)
    print("+" * 30)
    sleep(sl)
    print(f"Your score is {score}/{len(questions)}")
    sleep(sl)
    print("+" * 30)


def play_again():
    sleep(sl)
    i = input("Play again?...(y/n) >>> ").lower()
    return i


while 1:
    system("clear")
    x = display_score(new_game())
    if x == "Q":
        break
    y = play_again()
    if y == "y":
        print()
        system("clear")
        continue
    else:
        break
