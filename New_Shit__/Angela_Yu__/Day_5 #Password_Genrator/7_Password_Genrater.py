from random import choice, shuffle #, randint
from os import system

print("Welcome to the Password Generator!")
letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like in your password?\n"))
number_count = int(input("How many numbers would you like in your password?\n"))

letters = list("ABCDEFGHIJKLMNOPURSTUVWXYZabcdefghijklmnopqrstuvwxyz")
symbols = list("""!@#$%^&*(){}[]:";'<>?,./_+=-~`""")
numbers = list("1234567890")

pass_characters = [letters, symbols, numbers]

let_c = 0
sym_c = 0
num_c = 0
rand_num = 0
password = []

# wrong version.

# password = ""

# for i in range(letter_count+symbol_count+number_count):
#     if rand_num == 0 and let_c <= letter_count:
#         password += choice(letters)
#     elif rand_num == 1 and sym_c <= symbol_count:
#         password += choice(symbols)
#     elif rand_num == 2 and num_c <= number_count:
#         password += choice(numbers)
#     rand_num = randint(0,2)

# while not (letter_count+symbol_count+number_count) == len(password):
#     if rand_num == 0 and let_c < letter_count:
#         password += choice(letters)
#         let_c += 1
#     elif rand_num == 1 and sym_c < symbol_count:
#         password += choice(symbols)
#         sym_c += 1
#     elif rand_num == 2 and num_c < number_count:
#         password += choice(numbers)
#         num_c += 1
#     rand_num = randint(0,2)

for i in range(letter_count):
    password += choice(letters)
for i in range(symbol_count):
    password += choice(symbols)
for i in range(number_count):
    password += choice(numbers)

shuffle(password)

system("cls")

print(f"\nHere is your Password 🔒: ", *password, sep="")

letters = None
symbols = None
numbers = None
pass_characters = None
let_c = None
sym_c = None
num_c = None
rand_num = None
password = None
