from os import system
import pandas

NATO_phonetic_alphabet = pandas.read_csv(
    "D:\Software\Python\\New_Shit__\Angela_Yu__\Day_26 #NATO_phonetic_alphabet\\NATO_alpha.csv"
)


NATO_phonetic_alphabet = {
    j.Character: j.NATOalpha for i, j in NATO_phonetic_alphabet.iterrows()
}

print(NATO_phonetic_alphabet, end="\n\n")

while 1:
    code = input("What is the word? ")
    if code == "$exit" or code == "$quit":
        system("cls")
        break
    elif code == "$clear":
        system("cls")
        print(NATO_phonetic_alphabet)
        continue

    try:
        coded_word = " ".join([NATO_phonetic_alphabet[i] for i in code.upper()])
    except KeyError:
        print("Sorry, Only Alphanumeric characters are allowed.")
    else:
        print(coded_word)
