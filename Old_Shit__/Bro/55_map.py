store = [
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00),
    ("shoes", 200.00),
]

t_store = (
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00),
    ("shoes", 200.00),
)
to_euros = lambda data: (data[0], round(data[1] * 0.82,1))
to_us = lambda data: (data[0], round(data[1] / 0.82,1))

euros_store = list(map(to_euros, store))
us_store = list(map(to_us, t_store))

print(euros_store)
print(us_store)
