animal = 'cow'
item = "moon"
number = 3.14159

print("The {} jumped over the {}.".format(animal,item))
print("The {:10} jumped over the {:10}.".format(animal,item))
print("The {:^10} jumped over the {:>10}.".format(animal,item))
print("The {1} jumped over the {0}.".format(animal,item)) # positional argument
print("The {animal:^10} jumped over the {item}.".format(animal='moos',item="house")) # keyword argument
print(f"The {animal} jumped over the {item}.") # f string

print("The number pi is {:.2f}.".format(number))
print("The number $ is {:,}.".format(2000000000))
print("The number binary is {:b}.".format(2000000000))
print("The number otal is {:o}.".format(2000000000))
print("The number hex is {:X}.".format(2000000000))
print("The number scientific notation is {:e}.".format(2000000000))

