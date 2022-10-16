import sys
import timeit

mytuple = "max"
print(type(mytuple))

mytuple = ("max",)
print(type(mytuple))

mytuple = tuple(["max", 28, "Boston"])
print(type(mytuple))
print(mytuple)

item = mytuple[-1]
print(item)

for i in mytuple:
    print(i)

if "max" in mytuple:
    print("yes")

my_tuple = ("a", "p", "p", "l", "e")
print(len(my_tuple))
print(my_tuple.count("p"))
print(my_tuple.index("p"))

mylist = list(my_tuple)
print(mylist)

my_tuple = tuple(mylist)
print(my_tuple)


item = [i for i in range(1, 11)]
b = item[2:5]

print("b :", b, sep="-")

mytuple = "max", 28, "Boston"

name, age, city = mytuple

print(name)
print(age)
print(city)

mytuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

i1, *i2, i3 = mytuple
print(i1)
print(i2)
print(i3)

print()
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

print(timeit.timeit(stmt = "[0,1,2,3,4,5]",number=1000000))
print(timeit.timeit(stmt = "(0,1,2,3,4,5)",number=1000000))
