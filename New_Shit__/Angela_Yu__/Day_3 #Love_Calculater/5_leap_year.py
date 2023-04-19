while 1:
    year = input("Enter a year : ")
    if year == "exit":
        print("Exiting...")
        break

    if int(year) % 4 == 0:
        print("leap year...")
    else:
        print("Not leap year...  ")
    print()
