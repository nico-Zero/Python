from itertools import count
import random
import sys


def mygenerator():
    l = list(range(0, 101, 10))
    l.reverse()
    for i in l:
        yield i
    # yield 2
    # yield 3
    # yield 4
    # yield 5
    # yield 6
    # yield 7


g = mygenerator()

# for i in g:
#     print()
#############################################

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)
###########################################
# for i in g:
#     print(i)
###########################################

# print(sum(g))
# print(sorted(g))
###########################################

# def countdown(num):
#     print("Starting")
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(10)
# # for i in cd:
# #     print(i)

# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
###########################################


# def rand():
#     x = 0
#     y = 5
#     for _ in count(0):
#         yield random.randrange(x, y)
#         x += 5
#         y += 5

# r = rand()

# x=0
# i_times = 20
# for i in r:
#     print(i)
#     x+=1
#     if x > i_times:
#         break

###########################################

# def firstn(n):
#     r = []
#     num = 0
#     while num < n:
#         r.append(n)
#         num += 1
#     return r

# def firstn_g (n):
#     num = 0
#     while num < n:
#         yield n
#         num += 1

# print(sys.getsizeof(firstn(1000000)))
# print(sys.getsizeof(firstn_g(1000000)))

###########################################

# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b

# fib = fibonacci(int(input("Enter a number: ")))

# for i in fib:
#     print(i)

###########################################

# myg = (i for i in range (1000000) if i % 2 == 0) # return's by yield
# # for i in myg:
# #     print(i) 

# print(sys.getsizeof(myg))
# print()
# myl = [i for i in range(1000000) if i % 2 ==0] # return's by return

# # for i in myl:
# #     print(i)

# print(sys.getsizeof(myl))