mylist = ["yuvraj", "cherry", "apple"]

print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])

mylist2 = [5, True, "apple", "apple"]

item = mylist[0]

print(item)

for i in mylist:
    print(i)


if "yuvraj" in mylist:
    print("yes")
else:
    print("no")


print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("cherry")

print(mylist)

mylist.reverse()
print(mylist)

mylist = [23, 442, 21, 23, 1, 0]

mylist.sort()
print(mylist)

new_list = sorted(mylist)

print(mylist)
print(new_list)

mylist = [9] * 5
print(mylist)

mylist = [1, 2, 3, 4, 5]
new_list = new_list + mylist
print(new_list)

x = mylist[1:5]
print(x)

a = mylist[::2]
print(a)

list_org = ["banana", "cherry", "orange", "apple"]

list_cop = list_org.copy()  # using copy function
list_cop = list(list_org)  # using list funciton
list_cop = list_org[:]  # using slicing

list_cop.append(90)

print(list_cop)
print(list_org)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i * i * i for i in a]

print(b)

