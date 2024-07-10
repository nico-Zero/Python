# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)

def rec(m,n):
    print("*"*m,sep="", end="")
    print(("*"+(" "*(m-2))+"*\n")*n, sep="", end="")
    print("*"*m, sep="", end="")

rec(10,8)
