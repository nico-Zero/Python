print("Welcome to Python pizza Deliveries!")
prices = {"S" : 15,"M" : 20,"L" : 25}

size = input("What size pizza do you want? S, M, or L ? ")
add_pepperoni = input("Do you want pepperoni? Y or N ? ")
extra_cheese = input("Do you want extra cheese? Y or N ? ")

total = prices[size]
if add_pepperoni == " Y":
    if size == "S":
        total += 2
    else:
        total += 3
if extra_cheese == "Y":
    total += 1

print(f"Your final bill is: ${total}")
