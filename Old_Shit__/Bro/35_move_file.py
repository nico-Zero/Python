import os

d = "/media/zero/Software/__/text.txt"
s = "/media/zero/Software/__/Python/Bro/text.txt"

try:
    if os.path.exists(s):
        print("There is already a file there...")
    else:
        os.replace(d,s)
        print(s,"was moved...")
except FileNotFoundError:
    print('Source was not found...')

