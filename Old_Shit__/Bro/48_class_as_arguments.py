
class Car:
    color = None
class Motorcycle:
    color = None

def change_color(x,color):
    x.color = color

car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motorcycle()

change_color(car1,"black")
change_color(car2,"pink")
change_color(car3,"red")
change_color(bike1,"green")

print(car1.color)
print(car2.color)
print(car3.color)
print(bike1.color)
