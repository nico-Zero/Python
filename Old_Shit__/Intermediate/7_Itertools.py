from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat
import operator

# product
a = [1,2]
b = [3,4]
p = product(a,b, repeat= 2)

print(list(p))

#permutations
a = [1,2,3,4,5,6,7,8,9,10]
p = permutations(a , 10)

print(len(list(p)))

# combinations
a = [1,2,3,4,5,6,7,8,9,10]
c = combinations(a , 2)

print(list(c))
comb_wr = combinations_with_replacement(a,2)

print(list(comb_wr))

# accumulate

a = range(1,11)
acc = accumulate(range(1,11),func = operator.mul)
print(list(a))
print(list(acc))

# groupby

def smaller_than_3(x):
    return x< 3

a = [1,2,3,4,5]
group = groupby(a , key=smaller_than_3)
for key, value in group:
    print(key , list(value))

# infinite iterators
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in count(10):
    print(i)
    if i == 10000:
        break
# for i in cycle(a):
#     print(i)

for i in repeat(1,10):
    print(1)