from random import randint
def dice():
    return randint(1,7)

def convertRole():
    role = dice()
    while role > 5:
        print(role)
        role = dice()

    return role

# for _ in range(10):
#     print()
#     print(convertRole())

def dice5():
    return randint(1,5)

def convertRole7():
    role = dice5() + dice5()
    while role > 7:
        role = dice5() + dice5()
    return role
print(convertRole7())
