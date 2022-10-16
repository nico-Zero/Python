# happy = True
# print(happy)

# # walrus
# print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like? ")
#     if food =="q":
#         break
#     foods.append(food)

foods = list()
while (food := input("What food do you like? "))!= 'q':
    foods.append(food)

print(foods)