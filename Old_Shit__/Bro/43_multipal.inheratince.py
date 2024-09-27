from pyparsing import PrecededBy


class Prey:

    def flee(self):
        print("This animal flees.")

class Pradator:

    def hunt(self):
        print("This animal is hunting.")

class Rabbit(Prey):
    def run(self):
        print("This rabbit is runntin.")

class Hawk(Pradator):
    def fly(self):
        print("This haek is flying.")

class Fish(Prey,Pradator):
    def swim(self):
        print("This fish is swiming.")

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.run()
rabbit.flee()
hawk.fly()
hawk.hunt()
fish.swim()
fish.flee()
fish.hunt()

