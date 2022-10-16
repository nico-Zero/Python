while 1:
    number = input("Enter a number: ")

    if number == "exit":
        print("Exiting...")
        break
    elif int(number) % 2 == 0:
        print("Your number is Even number.")
    else:
        print("Your number is Odd number.")
