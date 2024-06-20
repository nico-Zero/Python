import matplotlib.pyplot as plt
import numpy as np

# print("hello, World !!!")

def f(x):
    return x**2 + x + 1

# make data
x_1 = np.linspace(start=-3, stop=3, num=100)
# [print(x) for x in x_1]
# x = (x for x in x_1)
# print( next(x) )

plt.plot(x_1, f(x_1))
plt.show()
