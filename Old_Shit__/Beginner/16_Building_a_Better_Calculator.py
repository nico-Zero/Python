num1 = float(input("Enter first number : "))
op = input("Enter a operater : ")
num2 = float(input("Enter second number : "))
input = 0

if op == "+":
    input = num1 + num2
elif op == "-":
    input = num1 - num2
elif op == "*":
    input = num1 * num2
elif op == "%":
    input = num1 % num2
elif op == "/":
    input = num1 / num2
else:
    print("Error: Unknown op")

if input != 0 :
    print(": " + str(input))
 