class Animal():

    alive = True

    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is slepping.")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit eat grass and carrot.")
    def run(self):
        print("This rabbit is running.")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming.")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying.")


rabbit = Rabbit()
rabbit.eat()