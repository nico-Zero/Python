def sqrt(num):
    i = 1
    while True:
        if i ** 2 > num:
            return i - 1
        else:
            i += 1


print(sqrt(6969))
