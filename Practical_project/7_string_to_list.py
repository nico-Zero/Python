def more():
    while True:
        more = input("Search more? (y/n): ")
        if more in ["y", "n"]:
            return more
        else:
            print("There an error in the input!!!")


def main():
    while True:
        string = input("Enter a string:- ")
        if string in ["exit", "quit", ":q", "/q"]:
            break
        the_list = [*string]
        print(the_list)
        print()
        if more() == "y":
            continue
        else:
            break


main()
