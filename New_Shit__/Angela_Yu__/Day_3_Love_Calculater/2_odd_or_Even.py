while 1:
    number = input("Enter a number: ")

    if number == "exit":
        print("Exiting...")
        break
    elif int(number) % 2 == 0:
        print("It's an even number.")
    else:
        print("It's a odd number.")
