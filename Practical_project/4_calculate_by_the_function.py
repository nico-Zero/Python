from math import factorial

def more():
    while True:
        more = input("Search more? (y/n): ")
        if more in ["y", "n"]:
            return more
        else:
            print("There an error in the input!!!")


def calculate(num):
    print("The Function is 1 + (1 / 1!) + (1 / 2!) + (1 / num!).")
    return 1 + (1 / 1) + (1 / 2) + (1 / factorial(num))


def main():
    while True:
        while True:
            str_num = input("Enter a number:- ")
            if str_num.isnumeric():
                num = int(str_num)
                break
            else:
                print("There is an error in the input!!!")

        print(f"The number {num}'s answer is :-", calculate(num))  # type: ignore
        print()
        if more() == "y":
            continue
        else:
            break

main()
