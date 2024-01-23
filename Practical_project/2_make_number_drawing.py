def print_drawing(num):
    drawing = [[j for j in range(1, i + 1)] for i in range(1, num + 1)]
    for x in drawing:
        print(*x)


def more():
    while True:
        more = input("Search more? (y/n): ")
        if more in ["y", "n"]:
            return more
        else:
            print("There an error in the input!!!")


def main():
    while True:
        while True:
            str_num = input("Enter a number:- ")
            if str_num.isnumeric():
                num = int(str_num)
                break
            else:
                print("There is an error in the input!!!")

        print_drawing(num)  # type: ignore
        print()

        if more() == "y":
            continue
        else:
            break


main()
