# numbers = range(1, int(input("Enter a number:- ")))
# numbers = [i * 2 for i in numbers]

# print(*numbers)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddis"]

ok_names = [i for i in names if len(i) <= 4]
Okay_names = [i.upper() for i in names if len(i) >= 5]

# print(ok_names)
print(Okay_names)
