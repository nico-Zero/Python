from pickle import NONE

class Car:
    wheels = 4
    def __init__(self, make, modle, year, color):
        self.make = make
        self.modle = modle
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.modle} is driving.")

    def stop(self):
        print(f"This {self.modle} is stopped")


car1 = Car("Sports", "Zila", 2069, "Crimson")
car2 = Car("Jipsi", "Jone", 2067, "Crimson-pink")

car1.wheels = 2
car1.drive()
print(car1.make)
print(car1.modle)
print(car1.year)
print(car1.color)
print(car1.wheels)
car1.stop()

print()

car2.drive()
print(car2.make)
print(car2.modle)
print(car2.year)
print(car2.color)
print(car2.wheels)
car2.stop()

