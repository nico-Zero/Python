# write

text = "Yoooo, this is busting."
try:
    with open("/media/zero/Software/__/Python/Bro/text.txt","w") as file:
        file.write(text)
except FileNotFoundError:
    print("That file is not found ):")

# append
text = "\nYoooo, I would like some ass."
try:
    with open("/media/zero/Software/__/Python/Bro/text.txt","a") as file:
        file.write(text)
except FileNotFoundError:
    print("That file is not found ):")
