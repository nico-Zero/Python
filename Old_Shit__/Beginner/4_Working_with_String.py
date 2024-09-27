from ast import For
from cmath import phase
import os

os.system("clear")

phrase = "The God"
print("The\nGod")
print('\nThe"God')
print("The\God")
print(phrase)
print(phrase + " is cool")
print(phrase.lower())  # It turns the whole string into lower.
print(phrase.upper())  # It turns the whole string into upper.
print(phrase.islower())  # It check's the whole string islower.
print(phrase.upper().isupper())  # It check's the whole string isupper.
print(len(phrase))  # Checks the length of the string.
print(phrase[0] + " " + phrase[2])  # Printing single value form the string.
print(phrase.index("G"))  # Printing the index of a character or word from a string.
print(phrase.replace("The", "Crappy"))  # Replacing something with something.
