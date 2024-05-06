from random import randint


def bubble_sort(_list):
    if not len(_list):
        raise ValueError("Need to pass a list with unsorted numbers.")
    for n in range(len(_list) - 1, 0, -1):
        for i in range(n):
            if _list[i] > _list[i + 1]:
                _list[i], _list[i + 1] = (
                    _list[i + 1],
                    _list[i],
                )
    return _list


unsorted = [randint(1, 1000) for _ in range(int(input("Enter Number :-")))]
sorted_list = bubble_sort(unsorted)

print(sorted_list)
