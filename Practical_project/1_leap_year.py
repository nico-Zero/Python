def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False


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
            srt_year = input(
                "Enter a Year to check :- ",
            )
            if srt_year.isnumeric():
                if len(srt_year) > 4:
                    srt_year = srt_year[:4]
                year = int(srt_year)
                break
            else:
                print("There is an error in the input!!!")

        print(f"Year {year} is a", "Leap Year." if leap_year(year) else "Not a Leap Year.")  # type: ignore
        print()

        if more() == "y":
            continue
        else:
            break


main()
