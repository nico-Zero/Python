def more():
    while True:
        more = input("Search more? (y/n): ")
        if more in ["y", "n"]:
            return more
        else:
            print("There an error in the input!!!")


def factors(num):
    factors_ = []
    for i in range(1, num):
        if num % i == 0:
            factors_.append(i)
    return factors_


def main():
    while True:
        while True:
            str_num = input("Enter a number:- ")
            if str_num.isnumeric():
                num = int(str_num)
                break
            else:
                print("There is an error in the input!!!")

        factors_answer = factors(num)  # type: ignore

        print(
            f"The Factors of {num}",  # type: ignore
            "is" if len(factors_answer) <= 1 else "are",
            factors_answer,
            ".",
        )
        print()
        if more() == "y":
            continue
        else:
            break


main()
