def make_tree(num):
    for i, j in zip(range(num), range(num-1, -1, -1)):
        print(" " * (j), "*" * ((i * 2) + 1))


make_tree(10)
