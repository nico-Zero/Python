def more():
    while True:
        more = input("Search more? (y/n): ")
        if more in ["y", "n"]:
            return more
        else:
            print("There an error in the input!!!")


def take_input(num):
    data = []
    for i in range(1, num + 1):
        while True:
            str_num = input(f"Enter a number {i} :- ")
            if str_num.isnumeric():
                data.append(int(str_num))
                break
            else:
                print("There is an error in the input!!!")
    return data


def largest_number(num_list: list) -> int:
    return max(num_list)


def main():
    while True:
        input_ = take_input(3)
        print(f"The largest number in {input_} is {largest_number(input_)}")
        print()
        if more() == "y":
            continue
        else:
            break


main()
