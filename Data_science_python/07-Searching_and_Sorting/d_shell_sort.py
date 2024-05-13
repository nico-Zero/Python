from random import  randint
from c_insertion_sort import insertion_sort 

def shell_sort(sort_list):
    word = [4,2]
    for i in word:
        for j in range(i):
            c_dict = {}
            while True:
                if j < len(sort_list):
                    c_dict[j] = sort_list[j]
                else:
                    c_dict = insertion_sort(c_dict)
                    for q,w in c_dict.items(): #type: ignore
                        sort_list[q] = w
                    break
                j += i
        # print(sort_list)
    return insertion_sort(sort_list)

x = [randint(1,1000) for _ in range(20)]

print("Unsorted:- ")
print(x)

sorted_list = shell_sort(x)

print("Sorted:- ")
print(sorted_list)

