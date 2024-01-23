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


def factors(num):
    factors_ = []
    for i in range(1, num):
        if num % i == 0:
            factors_.append(i)
    return factors_


def greatest_common_factor(num_list):
    check = []
    common_factor = []
    for i in num_list[0]:
        for x in num_list[1:]:
            if i in x:
                check.append(True)
            else:
                check.append(False)
        if all(check):
            common_factor.append(i)
        check = []
    return max(common_factor)


def main():
    while True:
        data = take_input(2)
        factors_of_data = [
            factors(data[0]),
            factors(data[1]),
        ]

        GCD = greatest_common_factor(factors_of_data)
        print(f"Greatest Common Factor of {data} is {GCD}")
        print()
        if more() == "y":
            continue
        else:
            break


main()
