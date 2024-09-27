from random import randint
def quickSort(unlist, maxmum_num):
    pivot = maxmum_num
    right = len(unlist) - 1
    left = 0

    if right < 1:
        return unlist

    while not (left == right or left > right):
        if unlist[right] < unlist[pivot]:
            unlist[pivot], unlist[right] = unlist[right], unlist[pivot]
            right -= 1
            continue
        elif unlist[left] > unlist[pivot]:
            unlist[pivot], unlist[left] = unlist[left], unlist[pivot]
            left += 1
            continue
        else:
            right -= 1
            left += 1

    return quickSort(unlist[:pivot], 0) + quickSort(unlist[pivot:], 1)

print(quickSort([randint(1,10000) for _ in range(20)],0))
