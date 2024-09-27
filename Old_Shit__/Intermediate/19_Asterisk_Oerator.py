result = 5**7
print(result)

zeros = [list(range(10))] * 10
# print(zeros)

print("AB" * 10)

func = [1, 2, 3]

print(*func, sep=",")

number = [1, 2, 3, 4, 5, 6]
*x, y, j = number
print(x, y, j)

print(number.pop())
print(number)

m = [*func, *number]
print(m)

