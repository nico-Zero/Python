ran = int(input("Enter a range : "))

for i in range(0, ran):
    if i % 3 == i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print("❌" * i)
