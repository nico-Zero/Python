# # from random import shuffle

# # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# # def s_ordered_search(s_list, l):
# #     for i, n in enumerate(s_list):
# #         if n <= l:
# #             if n == l:
# #                 return i
# #             continue
# #         else:
# #             return None


# # def s_unordered_search(s_list, l):
# #     for i, n in enumerate(s_list):
# #         if n == l:
# #             return i
# #     return None


# # jj = s_ordered_search(x, 9)
# # print("Ordered search :- ", jj)

# # shuffle(x)

# # jj = s_unordered_search(x, 9)
# # print("Unordered search :- ", jj)


# def main(search_list, find, left=0, right=0):
#     mid = (left + right) // 2
#     if search_list[mid] == find:
#         return mid
#     elif search_list[mid] < find:
#         return main(search_list, find, left=mid + 1, right=right)
#     else:
#         return main(search_list, find, left=left, right=mid - 1)


# def binary_search(l, f):
#     l = sorted(l)
#     result = main(l, f, left=0, right=len(l) - 1)
#     return result


# x = list(range(50, 100))
# location = binary_search(x, 69)
# print(location)

# import math


# def loop_Binary_search(search_list, find):
#     left = 0
#     right = len(search_list) - 1
#     while left != right:
#         mid = math.ceil((left + right) / 2)
#         if search_list[mid] < find:
#             left = mid
#         else:
#             right = mid - 1
#     if search_list[mid] == find:
#         return mid
#     return None


# x = list(range(50, 100))
# x.remove(69)
# location = loop_Binary_search(x, 68)
# print(location)