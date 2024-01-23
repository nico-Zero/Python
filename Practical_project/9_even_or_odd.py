def more():
    while True:
        more = input("Search more? (y/n): ")
        if more in ["y", "n"]:
            return more
        else:
            print("There an error in the input!!!")


def is_even(num):
    return True if num % 2 == 0 else False


def main():
    while True:
        while True:
            str_num = input("Enter a number:- ")
            if str_num.isnumeric():
                num = int(str_num)
                break
            else:
                print("There is an error in the input!!!")

        print(f"{num} is a", "Even" if is_even(num) else "Odd", "Number.")  # type: ignore
        print()
        if more() == "y":
            continue
        else:
            break


main()
