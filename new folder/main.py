for i in range(1, 1 + int(input("Enter a number:- "))):
    with open(f"new_folder_{i}", "w") as file:
        file.write(f"Fuck you {i}x")
