import os

os.system("cls")

x, y = 0, 0
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
tick_tak_toh = [row1, row2, row3]


check_element = [
    [[0, 0], [1, 1], [2, 2]],
    [[0, 2], [1, 1], [2, 0]],
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
]

all_element = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]


def update(map: list):
    os.system("cls")
    print(x, y)
    print(*map, sep="\n")


def core(player: str, x: int, y: int, symbol: str):
    try:
        if x == -1 or y == -1:
            raise Exception("Wrong Position")
        tick_tak_toh[x][y]
    except:
        update(tick_tak_toh)
        print("You entered a wrong position. ")
        if symbol == "X" or symbol == "〇":
            turn(player)
            insert(symbol)
        return

    if not tick_tak_toh[x][y] == "⬜":
        update(tick_tak_toh)
        if tick_tak_toh[x][y] == "X":
            print(f"{player1} marked this place already.")
        else:
            print(f"{player2} marked this place already.")

        turn(player)
        insert(symbol)
        update(tick_tak_toh)
    else:
        insert(symbol)


def turn(player):
    global x, y
    turn = input(f"{player} enter the cordinates :\n").split(",")
    if turn[0] == "exit":
        
        return 0
    try:
        x = int(turn[0]) - 1
        y = int(turn[1]) - 1
    except:
        x, y = 0, 0
        return


def insert(symbol):
    try:
        if tick_tak_toh[x][y] == "⬜":
            tick_tak_toh[x][y] = symbol
            update(tick_tak_toh)
    except:
        update(tick_tak_toh)


def check(sy):
    for i in check_element:
        if (
            tick_tak_toh[i[0][0]][i[0][1]] == sy
            and tick_tak_toh[i[1][0]][i[1][1]] == sy
            and tick_tak_toh[i[2][0]][i[2][1]] == sy
        ):
            return 1


while 1:
    player1 = input("What is your name player-1?\n") or "Player1"
    player2 = input("What is your name player-2?\n") or "Player2"

    update(tick_tak_toh)
    while 1:
        j = 0
        if turn(player1) == 0:
            break

        core(player1, x, y, "X")

        if check("X") == 1:
            print(f"\n{player1} win...")
            break

        if turn(player2) == 0:
            break

        core(player2, x, y, "〇")

        if check("〇") == 1:
            print(f"\n{player2} win...")
            break

        n = all(
            [
                True if not tick_tak_toh[i[0]][i[1]] == "⬜" else False
                for i in all_element
            ]
        )
        if n:
            print("\nIt's a tie!")
            break
    qu = input("""Would you like to play again? (Y/N)? """).lower()
    if not qu == "y":
        break
