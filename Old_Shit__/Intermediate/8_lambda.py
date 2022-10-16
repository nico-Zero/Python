from functools import reduce


add10 = lambda x : x+ 10
print(add10(5))

mult = lambda x,y : x *y
print(mult(7,9))

#sorted
point = [(1,2),(15,3),(5,-3),(90,33)]
point_shorted = sorted(point, key= lambda x: x[1] )

print(point)
print(point_shorted)

# map

a = range(1,10)
b = map(lambda x: x*2,a) 

print(list(b))

c = [ x*5 for x in a ]
print(list(c))

#filter
b = filter(lambda x:x%2 == 0,a)
print(list(b))

c = [x for x in a if x%2 ==0]
print(list(c))

#reduce

b = reduce(lambda x,y: x *y,a)
print(b)
