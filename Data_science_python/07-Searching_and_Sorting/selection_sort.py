from random import randint


def find_min(search_list):
    min = 0
    for i, j in enumerate(search_list):
        if j < search_list[min]:
            min = i
        else:
            continue
    return min


def selection_sort(sort_list):
    for i in range(len(sort_list)):
        min_i = find_min(sort_list[i:])
        sort_list[i], sort_list[min_i + i] = sort_list[min_i + i], sort_list[i]
    return sort_list

x = [randint(1, 1000) for _ in range(20)]

print(selection_sort(x))
