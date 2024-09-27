from math import ceil
from random import randint


def mearge(a,b):
    ci_a = 0
    ci_b = 0
    result = []
    while not (ci_a == len(a) and ci_b == len(b)):
        if ci_a < len(a) and ci_b < len(b):
            if a[ci_a] < b[ci_b]:
                result.append(a[ci_a])
                ci_a += 1
            else:
                result.append(b[ci_b])
                ci_b += 1
        else:
            if ci_a < len(a):
                result.append(a[ci_a])
                ci_a += 1
            else:
                result.append(b[ci_b])
                ci_b += 1
    return result

def mearge_sort(the_list):
    mid = ceil(len(the_list)/2)
    if mid == 0 :
        return []
    elif len(the_list) == 1:
        return the_list
    else:
        a = mearge_sort(the_list[:mid])
        b = mearge_sort(the_list[mid:])
        return mearge(a,b)

x = [randint(1,1000) for _ in range(21)]
print(x)
x = mearge_sort(x)
print(x)
