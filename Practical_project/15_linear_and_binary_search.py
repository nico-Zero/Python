def linear_search(unsorted_list, search_for):
    for index, value in enumerate(unsorted_list):
        if value == search_for:
            return index
    return None


def mid_value(low, high):
    return low + (high - low) // 2


def binary_search(unsorted_list, search_for):
    low = 0
    high = len(unsorted_list) - 1
    mid = mid_value(low, high)
    while True:
        if unsorted_list[mid] == search_for:
            return mid
        elif unsorted_list[mid] < search_for:
            low = mid + 1
            mid = mid_value(low, high)
        elif unsorted_list[mid] > search_for:
            high = mid - 1
            mid = mid_value(low, high)
        else:
            return None


def take_search_list():
    list_input = input("Enter a list:- ").split(",")
    data = [int(i) for i in list_input if i.isnumeric()]
    return data


def take_search_for(search_list):
    while True:
        str_search_for = input("Enter a Search for:- ")
        if str_search_for.isnumeric():
            search_for = int(str_search_for)
            if search_for in search_list:
                break
            else:
                print("Invalid Search for Item!!!")
                continue
        else:
            print("There is an error in the input!!!")
    return search_for


def take_search_type():
    search_types = ["binary", "linear"]
    print(f"Select one of this {search_types}.")
    while True:
        search_type = input("Enter a Search Type:- ")
        if search_type in search_types:
            return search_type
        else:
            continue


def more():
    while True:
        more = input("Search more? (y/n): ")
        if more in ["y", "n"]:
            return more
        else:
            print("There is an error in the input!!!")

def main():
    while True:
        search = {
            "linear": linear_search,
            "binary": binary_search,
        }
        search_list = take_search_list()
        search_type = take_search_type()
        search_for = take_search_for(search_list)

        print(
            f"Index of {search_for} in list {search_list} is {search[search_type](search_list,search_for)}",
            end="\n\n",
        )
        if more() == "y":
            continue
        else:
            break


main()