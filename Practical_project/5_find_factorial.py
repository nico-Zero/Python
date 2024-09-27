from functools import reduce


def more():
    while True:
        more = input("Search more? (y/n): ")
        if more in ["y", "n"]:
            return more
        else:
            print("There an error in the input!!!")


def factorial(num):
    answer = reduce(lambda x, y: x * y, range(1, num + 1))
    return answer


def main():
    while True:
        while True:
            str_num = input("Enter a number:- ")
            if str_num.isnumeric():
                num = int(str_num)
                break
            else:
                print("There an error in the input!!!")

        print(f"The Factorial of {num} is:- ", factorial(num))  # type: ignore
        print()
        if more() == "y":
            continue
        else:
            break


main()
