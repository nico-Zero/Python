from random import randint

def quick_sort(sort_list,p = None,left = None, right = None):
    p = 0 if p is None else p
    left = 0 if left is None else left
    right = len(sort_list) - 1 if right is None else right
    swit = True
    ci_l = left
    ci_r = right

    if right - left <= 1:
        return

    while True:
        if swit:
            if sort_list[left] > sort_list[p]:
                swit = False
            elif left == ci_r:
                swit = False
            else:
                left += 1
        else:
            if sort_list[right] < sort_list[p]:
                if right - left <= 0:
                    break
                if sort_list[left] > sort_list[right]:
                    sort_list[left],sort_list[right] = sort_list[right],sort_list[left]
                swit = True
            elif right == ci_l:
                break
            else:
                right -= 1

    if sort_list[p] > sort_list[right]:
        sort_list[p],sort_list[right] = sort_list[right],sort_list[p]
    quick_sort(sort_list, left = ci_l, right = right - 1, p = ci_l)
    quick_sort(sort_list, left = right + 1, right = ci_r , p = right + 1)

jj = 10

x = [randint(1,1000) for _ in range(jj)]

print("Unsorted :- ")
print(x)
print("Sorted :- ")
quick_sort(x)
print(x)
