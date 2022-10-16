def power(base_num, pow_num):
    i = 1
    for index in range(pow_num):
        i = i * base_num
    return i


print(power(3, 4))
