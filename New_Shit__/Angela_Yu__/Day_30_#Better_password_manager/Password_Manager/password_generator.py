from random import choice, shuffle, randint


def pass_gen(letters=randint(5, 8), symbols=randint(5, 8), numbers=randint(5, 8)):
    letter = list("ABCDEFGHIJKLMNOPURSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    symbol = list("""!@#$%^&*(){}[]:";'<>?,./_+=-~`""")
    number = list("1234567890")

    password = (
        [choice(letter) for _ in range(letters)]
        + [choice(symbol) for _ in range(symbols)]
        + [choice(number) for _ in range(numbers)]
    )

    shuffle(password)
    password = "".join(password)

    return password
