friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20)
]

get_drunk = lambda age: age[1] >= 18

drunk = list(filter(get_drunk,friends))
print(drunk)
