from os import system
from time import sleep

# Some Important Variables
coffee = {
    "espresso": {"water": 50, "coffee": 18, "milk": 0, "price": 1.50},
    "latte": {"water": 200, "coffee": 24, "milk": 150, "price": 2.50},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 3.00},
}
option = [
    {
        "e": "espresso",
        "espresso": "espresso",
        "l": "latte",
        "latte": "latte",
        "c": "cappuccino",
        "cappuccino": "cappuccino",
    },
    "report",
    "r",
]

logo = {"espresso": "🍼", "latte": "🍵", "cappuccino": "🍷"}
water_capacity = 300
coffee_capacity = 100
milk_capacity = 200

coins = {"p": 0.01, "n": 0.05, "d": 0.10, "q": 0.25}
profit = 0
i = 0

# Few function for the program


def report():
    return f"""water: {water_capacity}ml\nMilk: {milk_capacity}ml
Coffee: {coffee_capacity}g\n"""


def price(item):
    return coffee[option[0][item]]["price"]


def check_quantity(item):
    global water_capacity, coffee_capacity, milk_capacity

    quantity = [
        water_capacity - coffee[option[0][item]]["water"],
        coffee_capacity - coffee[option[0][item]]["coffee"],
        milk_capacity - coffee[option[0][item]]["milk"],
    ]
    if quantity:
        if quantity < [0, 0, 0]:
            print("We can't make what you want right now.")
            return True
        else:
            water_capacity = quantity[0]
            coffee_capacity = quantity[1]
            milk_capacity = quantity[2]
            return False


def coin():
    global string
    inserted_coin = input("Please enter coins: ")
    string = inserted_coin
    inserted = round(sum([coins[i] if i in coins else 0 for i in string]), 2)
    return inserted


system("cls")
# Main loop
while 1:
    # The second main loop
    while 1:
        i = input("What would you like? (espresso/latte/cappuccino): ")
        if i == "off":
            break

        if i not in option and i not in option[0]:
            system("cls")
            continue

        if check_quantity(i):
            break

        else:
            print(f"Your total will be: ${price(i)}")
            profit += price(i)
            print(*coins.items())

            inserted = coin()
            change = round((inserted - price(i)), 2)
            while change < 0:
                if change < 0:
                    print(f"You entered {abs(change)} less.")
                    inserted = coin()
                    change = round((inserted - abs(change)), 2)

            if not change <= 0:
                print(f"Your change will be {change}.")

            print(f"Here is your {logo[option[0][i]]} {option[0][i]}")
            break

    x = input("Would you like to buy another coffee? Y/N: ").lower()
    system("cls")
    if x == "n":
        system("cls")
        break

    elif x == "admin" or x == "owner":
        check = input("What you like to check money or tanks? ").lower()

        if check == "money" or check == "m":
            print(f"Your total profit is ${profit}")
            if input("Do you want to collect the money? Y/N ?").lower() == "y":
                profit = 0
                system("cls")
            else:
                sleep(5)
                system("cls")
                pass

        elif check == "tank" or check == "t":
            print(report())
            if input("Would you like to fill the tanks? Y/N: ").lower() == "y":
                water_capacity = 300
                coffee_capacity = 100
                milk_capacity = 200
                system("cls")
            system("cls")
        system("cls")
    else:
        system("cls")
