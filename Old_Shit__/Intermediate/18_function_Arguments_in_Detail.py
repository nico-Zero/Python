def p(n):
    print(n)

# p("zanda")

def foo(a, x, f, d=69):
    print(a, x, f)
    print(f"Fuck you and {d}")

# foo(1,2,3)
# foo(f=1,a=2,x=3)
# foo(1,f=2,x=3)

def foo(a, b, *x, **y):
    print(a, b)
    for arg in x:
        print(arg)
    for key in y:
        print(key, y[key])

# foo(1,2,3,4,5,6,7,8,9,10,11,six=6,seven=7,ten=10)

def foo(a, b, *, c, d):  # after the stars it will only accept keyword arguments
    print(a, b, c, d)

# foo(1, 2, c=3, d=4)

def x(*args, c, d):  # after the *args it will only accept keyword arguments
    for arg in args:
        print(arg)
    print(c, d)

# x(69,23,1983,223,23,c=69,d=96)

def flex(a, b, c):
    print(a, b, c)

lis = [1, 2, 3]
lis1 = (0, 9, 8)
dic = {"a": 0.1, "b": 0.2,"c": 0.3};

# flex(*lis)  # The star unpacks the list into the function arguments.
# flex(*lis1)  # It also works with tuple.
# flex(**dic) # keys must to same as fucntion arguments.

def fff():
    # global number
    # x = number
    number =4
    print(f"number inside fucntion {x}")

number = 69
# fff()
# print(number)


####################################################
def ff(x,lis):
    lis.append(69)
    x = 5
lis = [1,2,3]
var =10
ff(var,lis)
print(var)
print(lis)
