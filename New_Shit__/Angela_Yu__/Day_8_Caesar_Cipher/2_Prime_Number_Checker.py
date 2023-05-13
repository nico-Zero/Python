def prime_checker(number):
    for i in range(2,number):
        if number % i == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number")
while 1:
    x = int(input("Enter a number: "))
    prime_checker(x)
