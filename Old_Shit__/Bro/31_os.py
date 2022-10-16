import os

path = "/media/zero/Software/__/Python/Bro"

if os.path.exists(path):
    print("Yes it does.")
    if os.path.isfile(path):
        print("That is a file.")
    elif os.path.isdir:
        print("That is a directory.")
    else:
        print("And no it's not a file.")
else:
    print("No it doesn't.")
    