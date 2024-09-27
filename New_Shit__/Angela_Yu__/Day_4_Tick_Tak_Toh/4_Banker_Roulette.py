import random

name = input("Give me everybody's name, seperated by a comma. \n")
name_list = name.split(",") 

print(f"{random.choice(name_list)} is going to buy the meal today!")

