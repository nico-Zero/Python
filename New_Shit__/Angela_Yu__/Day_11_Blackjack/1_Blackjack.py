from prettytable import PrettyTable
from random import choice
from os import system

# Important variables
shape = ["♣", "◆", "❤", "♠"]
card_numbers = [
    (2, " "),
    (3, " "),
    (4, " "),
    (5, " "),
    (6, " "),
    (7, " "),
    (8, " "),
    (9, " "),
    (1, 0),
    ("J", " "),
    ("Q", " "),
    ("K", " "),
    ("A", " "),
]
card_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}

back = """
    ┌─────────┐
    │░░░░░░░░░│
    │░░░░░░░░░│
    │░░░░░░░░░│
    │░░░░░░░░░│
    │░░░░░░░░░│
    │░░░░░░░░░│
    │░░░░░░░░░│
    └─────────┘
"""
table = PrettyTable()
table.border = False
table.header = False

# Function part is from here.
# Function makes the cards structures.


def card(c_n, c_s):
    return f"""
    ┌─────────┐
    │ {c_n[0]}{c_n[1]}      │
    │         │
    │         │
    │    {c_s}    │
    │         │
    │         │
    │       {c_n[0]}{c_n[1]}│
    └─────────┘
    """


again = False

# Deals a random card returns a tuple out.


def random_card():
    return (choice(card_numbers), choice(shape))


# Updates the values of the cards.
def update_values():
    global p_value, c_value
    p_value = [
        card_values[i[23] + i[24]] if i[24] == "0" else card_values[i[23]]
        for i in player_cards
    ]
    if 11 in p_value and sum(p_value) > 21:
        p_value = [1 if i == 11 else i for i in p_value]

    c_value = [
        card_values[i[23] + i[24]] if i[24] == "0" else card_values[i[23]]
        for i in computer_cards
    ]
    if 11 in c_value and sum(c_value) > 21:
        c_value = [1 if i == 11 else i for i in c_value]


# Calculate the total points for each player every time player hits.
def total_points():
    global t_p, t_c
    t_p = sum(p_value)
    t_c = sum(c_value)


# Checks if a player is busted or not.
def got_bust():
    if t_p > 21:
        system("cls")
        print_cards(0)
        print(player_name, "got busted.")
        return True
    elif t_c > 21:
        system("cls")
        print_cards(0)
        print(computer_name, "got busted.")
        return True
    return False


# Prints cards to the terminal
def print_cards(a=1):
    print(player_name, ":-")
    table.add_row(player_cards)
    print(table)

    table.clear()
    print(computer_name, ":-")
    if a:
        table.add_row(
            [computer_cards[0], *[back for i in range(len(computer_cards) - 1)]]
        )
        print(table)
        table.clear()
    else:
        table.add_row(computer_cards)
        print(table)
        table.clear()


# See's if somebody got a blackjack card or not.
def blackjack(x=1):
    global t
    if x == 1:
        if (
            11 in p_value
            and 10 in p_value
            and not (player_cards[0][24] == "0" or player_cards[1][24] == "0")
        ):
            system("cls")
            print_cards(0)
            print(player_name, "won with blackjack.")
            return True
        elif (
            11 in c_value
            and 10 in c_value
            and not (computer_cards[0][24] == "0" or computer_cards[1][24] == "0")
        ):
            system("cls")
            print_cards(0)
            print(computer_name, "won with blackjack.")
            return True
    t = 0
    return False


# The main game loop
while 1:
    # Now cls the screen and ask name of player and computer.
    system("cls")
    player_cards = [card(*random_card()), card(*random_card())]
    computer_cards = [card(*random_card()), card(*random_card())]
    player_name = input("What is your name? ").title() or "Player-1"
    computer_name = input("Computer name:- ").title() or "Computer"
    t = 1
    system("cls")
    update_values()
    total_points()

    # The second main game loop
    while 1:
        print_cards()
        if blackjack(t):
            break

        # Checking if player wants to hit or not.
        if_hit = input("Enter 'hit' for hit and 'stand' for stand:\n")

        if if_hit == "hit" or if_hit == "h":  # if player want to hit.
            player_cards.append(card(*random_card()))
            computer_cards.append(card(*random_card()))

        elif if_hit == "stand" or if_hit == "s":  # if player don't want to hit
            if t_c <= 17:
                computer_cards.append(card(*random_card()))
                update_values()
                total_points()
            system("cls")
            print_cards(0)
            if got_bust():
                break

            if (21 - t_p) < (21 - t_c):
                print(player_name, "win...")
            elif (21 - t_p) > (21 - t_c):
                print(computer_name, "win...")
            elif (21 - t_p) == (21 - t_c):
                print("It's a Draw")
            break

        # Update things below.
        update_values()
        total_points()
        print_cards()

        if got_bust():
            break

        system("cls")
    if input("Would you like to play again? (y/n): ").lower() == "n":
        break
