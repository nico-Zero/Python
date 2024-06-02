from functools import reduce

x = ''
while not x.isnumeric():
    x = input("Enter some number:- ")

x = [int( i ) for i in x]
x = sorted(x)[-3:]
ans = reduce(lambda x, y: x * y, x)

print(ans)
