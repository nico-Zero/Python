lucky_number = [4, 8, 42, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]

# friends.extend(lucky_number)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Jim")
print(friends)
friends.pop()
print(friends)
print(friends.index("Kevin"))
print(friends.count("Jim"))

friends.sort()
print(friends)

lucky_number.sort()
print(lucky_number)

lucky_number.reverse()
print(lucky_number)

friends2 = friends.copy()
print(friends2)

# friends.clear()
# print(friends)
