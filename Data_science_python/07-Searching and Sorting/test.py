from random import shuffle

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def s_ordered_search(s_list, l):
    for i, n in enumerate(s_list):
        if n <= l:
            if n == l:
                return i
            continue
        else:
            return None


def s_unordered_search(s_list, l):
    for i, n in enumerate(s_list):
        if n == l:
            return i
    return None


jj = s_ordered_search(x, 9)
print("Ordered search :- ", jj)

shuffle(x)

jj = s_unordered_search(x, 9)
print("Unordered search :- ", jj)
