def insertion_sort(unsorted_list: list):
    counter = []
    while True:
        for i in range(len(unsorted_list)):
            if i != len(unsorted_list) - 1:
                if unsorted_list[i] > unsorted_list[i + 1]:
                    for j in range(i + 1, -1, -1):
                        if j != 0:
                            if unsorted_list[j] < unsorted_list[j - 1]:
                                unsorted_list[j], unsorted_list[j - 1] = (
                                    unsorted_list[j - 1],
                                    unsorted_list[j],
                                )
                                counter.append(False)
                        else:
                            break
                else:
                    counter.append(True)
        if all(counter):
            return unsorted_list
        else:
            counter.clear()


def bubble_sort(unsorted_list: list):
    counter = []
    while True:
        for i in range(len(unsorted_list)):
            if i != len(unsorted_list) - 1:
                if unsorted_list[i] > unsorted_list[i + 1]:
                    unsorted_list[i], unsorted_list[i + 1] = (
                        unsorted_list[i + 1],
                        unsorted_list[i],
                    )
                    counter.append(False)
                else:
                    counter.append(True)
        if all(counter):
            return unsorted_list
        else:
            counter.clear()


def selection_sort(unsorted_list: list):
    for i in range(len(unsorted_list)):
        mi = min(unsorted_list[i:])
        mi_index = unsorted_list[i:].index(mi) + i
        unsorted_list[mi_index], unsorted_list[i] = unsorted_list[i], mi
    return unsorted_list


def take_unsorted_list():
    list_input = input("Enter a list:- ").split(",")
    data = [int(i) for i in list_input if i.isnumeric()]
    return data


def take_sort_type():
    sort_types = ["insertion", "bubble", "selection"]
    print(f"Select one of this {sort_types}.")
    while True:
        search_type = input("Enter a Search Type:- ")
        if search_type in sort_types:
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
        sort = {
            "insertion": insertion_sort,
            "bubble": bubble_sort,
            "selection": selection_sort,
        }
        unsorted_list = take_unsorted_list()
        sort_type = take_sort_type()

        print(
            f"Unsorted list: {unsorted_list} and \nSorted list: {sort[sort_type](unsorted_list)}."
        )

        if more() == "y":
            print()
            continue
        else:
            break

main()
