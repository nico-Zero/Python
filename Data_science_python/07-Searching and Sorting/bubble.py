from random import randint


def bubble_sort(unsorted_list):
    if not len(unsorted_list):
        raise ValueError("Need to pass a list with unsorted numbers.")
    c = [False]
    while all(c) == False:
        c.clear()
        for i in range(1, len(unsorted_list)):
            if unsorted_list[i - 1] > unsorted_list[i]:
                unsorted_list[i - 1], unsorted_list[i] = (
                    unsorted_list[i],
                    unsorted_list[i - 1],
                )
                c.append(False)
            else:
                c.append(True)
    return unsorted_list


unsorted = [randint(1, 1000) for _ in range(int(input("Enter Number :-")))]
sorted_list = bubble_sort(unsorted)

print(sorted_list)



