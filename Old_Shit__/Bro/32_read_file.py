try:
    with open("/media/zero/Software/__/Python/Bro/text.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found ):")
