set_ = {1, 2, 3, 1, 2}
set__ = set("Hello")
set___ = set([1, 2, 3, 4, 5, 2, 1, 3, 4])

print(set_)
print(set__)
print(set___)


set_z = set()

set_z.add(1)
set_z.add(2)
set_z.add(3)
set_z.add(1)
set_z.add(2)

set_z.remove(3)

print(set_z)

for i in set___:
    print(i)


odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

u = odd.union(even)

print(u)

i = odd.intersection(even)
j = odd.intersection(prime)

print(i, j)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
diffx = setB.difference(setA)

print(diff)
print(diffx)

s_diff = setA.symmetric_difference(setB)
print(s_diff)

setA.update(setB)

print(setA)
setA.intersection_update(setB)

print(setA)

setA.difference_update(setB)

print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB))
print(setB.issubset(setA))

print(setA.issuperset(setB))
print(setB.issuperset(setA))

print(setA.isdisjoint(setB))


setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}


# setB = setA

# setB.add(7)

# print(setA)
# print(setB)

setB = setA.copy()

setB.add(7)

print(setA)
print(setB)

a = frozenset([1,2,3,4,5])

