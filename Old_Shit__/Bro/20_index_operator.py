from more_itertools import last


name = "nico_zero"
if (name[0]).islower:
    name = name.capitalize()
# print(name)

first_name = name[5:].capitalize()
last_name = name[:4]
# print(first_name,last_name)

first = name.split("_")
first.insert(2, "Nova")
print(first)
