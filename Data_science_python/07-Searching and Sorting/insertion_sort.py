from random import randint


def insertion_sort(the_list):
    for i in range(1, len(the_list)):
        if the_list[i - 1] > the_list[i]:
            for j in range(i, 0, -1):
                if the_list[j] < the_list[j - 1]:
                    the_list[j], the_list[j - 1] = the_list[j - 1], the_list[j]
                else:
                    break
    return the_list


x = [randint(1, 1000) for i in range(20)]

print(insertion_sort(x))
