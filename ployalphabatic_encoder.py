from os import system
from time import sleep

lower_alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
upper_alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")

encoded_data = []
decoded_data = []

while 1:
    data = input("Enter a string to encode:- ")
    for i, j in enumerate(data, start=1):
        if j == " ":
            encoded_data.append(" ")
            continue
        try:
            index_in_org = (lower_alphabet.index(j) + i) % 26
            encoded_data.append(lower_alphabet[index_in_org])
        except:
            index_in_org = (upper_alphabet.index(j) + i) % 26
            encoded_data.append(upper_alphabet[index_in_org])

    print("".join(encoded_data))

    if input("Would you like to decode:- ") in ("y", "yes"):
        data = input("Enter a string to decode:- ") or "".join(encoded_data)
        for i, j in enumerate(data, start=1):
            if j == " ":
                decoded_data.append(" ")
                continue
            try:
                index_in_org = (lower_alphabet.index(j) - i) % 26
                decoded_data.append(lower_alphabet[index_in_org])
            except:
                index_in_org = (upper_alphabet.index(j) - i) % 26
                decoded_data.append(upper_alphabet[index_in_org])

    print("".join(decoded_data))
    sleep(3)
    system("clear")

