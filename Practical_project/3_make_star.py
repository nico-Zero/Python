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
            str_star = input("Enter a number of Star:- ")
            if str_star.isnumeric():
                stat_num = int(str_star)
                break
            else:
                print("There is an error in the input!!!")

        for i in range(stat_num):  # type: ignore
            print("*" * i)
            print()
        if more() == "y":
            continue
        else:
            break


main()
