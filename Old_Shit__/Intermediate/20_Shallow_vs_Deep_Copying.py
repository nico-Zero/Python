import copy

# org = [list(range(1,4))] * 5
# cpy = copy.deepcopy(org)

# cpy[0][0] = -69
# print(cpy)
# print(org)

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

class Son:
    def __init__(self,name, age):
        self.name = name
        self.age = age

p1 = Person("Zero", 69)
p2 = copy.copy(p1)

p2.name = "Jain"
print("p2 :- ",p2.name)
print("p1 :- ",p1.name)
#########################################
son = Son(p1,p2)
son_c = copy.deepcopy(son)

son_c.name.name = "Xon"
print("son :- ",son_c.name.name)
print("son_c :-",son.name.name)

print("p2 :- ",p2.name)
print("p1 :- ",p1.name)