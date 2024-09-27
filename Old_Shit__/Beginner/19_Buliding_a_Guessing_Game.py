import os

sec = 69
geass = 0
g_count = 1
g_limit = 3

while sec != geass:

    if g_count <= g_limit:
        print("Turn : " + str(g_count))
        geass = int(input("Guess the secret number : "))
        g_count += 1
    else:
        break

    if sec != geass and g_count <= g_limit:
        os.system("clear")
    else:
        break

if sec == geass:

    print("\nYou win.")
else:
    print("\nYou lose.")
