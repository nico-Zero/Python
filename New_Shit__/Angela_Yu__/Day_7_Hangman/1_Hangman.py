from english_words import get_english_words_set
from PyDictionary import PyDictionary
from functools import reduce
from random import choice
from os import system
from logo import *

while 1:
    try:
        dict = PyDictionary()

        # All variables.
        random_word = choice(list(words))
        check = random_word

        # Finding the meaning of the random_word.
        x = dict.meaning(check)
        key = list(x.keys())
        meaning = x[key[0]][0].capitalize()
        system("clear")
        break
    except:
        system("clear")
        pass

len_random_word = len(random_word)
stage = "_" * len_random_word
stage_word = list(stage)
lifes = 6
half_life = lifes / 2
heart_bar = "❤️"
hangman_pose = 0


# The function which will update the CLI screen.
def update():
    print(hangman)
    print(HANGMAN[hangman_pose])
    if lifes <= half_life:
        print(f"Hint :- {key[0]} of the Word :", f"{meaning}.")
    else:
        print()
    print(heart_bar * lifes)
    print(" " * 6, " The word :", *stage_word, sep="")


update()

# The main funciton
while 1:
    if lifes > 0:
        # Taking input from the user.
        ans = input("\nGauss the word : ")[0]
        # You con quit by inputing exit.
        if ans == "exit":
            print("\nGame Over...")
            print("Come again to play with us.")
            break
        # Here we raplace random_word characters with gaussed characters.
        elif ans in random_word:
            l = random_word.find(ans)
            stage_word[l] = random_word[l]
            random_word = random_word.replace(ans, "_", 1)
        else:
            hangman_pose += 1
            lifes -= 1
        # Checking if the random_word and stage_word are equal or not.
        if reduce(lambda x, y: x + y, stage_word) == check:
            print("\nYou Win...")
            print("Fuck Yaaa babyy, I won...")
            break
        system("clear")
        update()
    else:
        print("\nGame Over...")
        print("Come again to play with us.")
        break
