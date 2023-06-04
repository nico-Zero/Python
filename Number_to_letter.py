from os import system

number = [
    "Zero",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
]
tenth = [
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
]
i_m_values = ["Hundred", "Thousand", "Lakh", "crore"]


def two_digit(num: int) -> str:
    if num <= 19:
        return number[num]
    elif num % 10 == 0:
        return tenth[int(num / 10) - 2]
    else:
        return tenth[int(num / 10) - 2] + " " + number[num % 10]


def three_digits(num: int, i_m: int) -> str:
    if num == 0:
        return ""
    elif num < 100:
        return two_digit(num)
    elif num % 100 == 0:
        return two_digit(int(num / 100)) + " " + i_m_values[i_m]
    else:
        return (
            two_digit(int(num / 100))
            + " "
            + i_m_values[i_m]
            + " "
            + two_digit(num % 100)
        )


system("clear")

while 1:
    if (num := input("What number would you like to convert? ")) == "clear":
        system("clear")
        continue

    elif num == "exit" or num == "quit":
        break

    try:
        num = int(num)
    except ValueError:
        print("Invalid number")
        continue

    l_num = len(str(num))

    # for two digit
    if l_num <= 2:
        print(two_digit(num), "\n")
        print()

    # for three or less digit
    elif l_num <= 3:
        print(three_digits(num, 0))
        print()

    # for five or less digit
    elif l_num <= 5:
        print(
            two_digit(int(num / 1000)),
            i_m_values[1],
            three_digits(num % 1000, 0),
        )
        print()

    # for seven or less digit
    elif l_num <= 7:
        if int(num / 1000) % 100 == 0:
            print(
                two_digit(int(num / 100000)),
                i_m_values[2],
                three_digits(num % 1000, 0),
            )
            print()

        else:
            print(
                two_digit(int(num / 100000)),
                i_m_values[2],
                two_digit(int(num / 1000) % 100),
                i_m_values[1],
                three_digits(num % 1000, 0),
            )
            print()

    # for ten or less digit
    elif l_num <= 10:
        # if both lakh and thousand are zero
        if int(num / 1000) % 100 == 0 and int(num / 100000) % 100 == 0:
            print(
                three_digits(int(num / 10000000), 0),
                i_m_values[3],
                three_digits(num % 1000, 0),
            )
            print()

        # if both thousand is zero and lakh is not
        elif int(num / 1000) % 100 == 0 and int(num / 100000) % 100 != 0:
            print(
                three_digits(int(num / 10000000), 0),
                i_m_values[3],
                two_digit(int(num / 100000) % 100),
                i_m_values[2],
                three_digits(num % 1000, 0),
            )
            print()

        # if both thousand is not zero but lakh is
        elif int(num / 1000) % 100 != 0 and int(num / 100000) % 100 == 0:
            print(
                three_digits(int(num / 10000000), 0),
                i_m_values[3],
                two_digit(int(num / 1000) % 100),
                i_m_values[1],
                three_digits(num % 1000, 0),
            )
            print()

        # when everything is Okay
        else:
            print(
                three_digits(int(num / 10000000), 0),
                i_m_values[3],
                two_digit(int(num / 100000) % 100),
                i_m_values[2],
                two_digit(int(num / 1000) % 100),
                i_m_values[1],
                three_digits(num % 1000, 0),
            )
            print()