def more():
    while True:
        more = input("Search more? (y/n): ")
        if more in ["y", "n"]:
            return more
        else:
            print("There an error in the input!!!")


def generate_fibonacci(num):
    current_number = 0
    fibonacci_series = []
    next_number = 1
    while current_number < num:
        fibonacci_series.append(current_number)
        current_number, next_number = next_number, current_number + next_number

    return fibonacci_series


def main():
    while True:
        while True:
            str_num = input("Enter a number:- ")
            if str_num.isnumeric():
                num = int(str_num)
                break
            else:
                print("There is an error in the input!!!")

        print("fibonacci series :- ", generate_fibonacci(num))  # type: ignore
        print()
        if more() == "y":
            continue
        else:
            break


main()
