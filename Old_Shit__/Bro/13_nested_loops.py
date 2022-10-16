from sympy import symbols


w = int(input("Enter number of column:- "))
h = int(input("Enter number of rows:- "))
symbol = str(input("Enter a symbol to use:- "))

for i in range(h):
    for j in range(w):
        print(symbol,end="")
    print()

