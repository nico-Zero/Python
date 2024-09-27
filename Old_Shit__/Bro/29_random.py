import random

x = random.randint(1,6)
y = random.random()
list = ["rock","paper","sicer"]

print(x)
print(y)
print(random.choice(list))

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)