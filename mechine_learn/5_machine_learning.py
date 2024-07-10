import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + x + 1

# make data
x_1 = np.linspace(start=-3, stop=3, num=100)
# [print(x) for x in x_1]
# x = (x for x in x_1)
# print( next(x) )

# plt.plot(x_1, f(x_1))
# plt.xlabel("x", fontsize=12)
# plt.ylabel("f(x)", fontsize=12)
# plt.show()


## Slope & Deritive of Function.
def df(x):
    return 2*x + 1


## Plot Function and deritive side by side.

plt.figure(figsize=(15,5))

## Plot 1

plt.subplot(1,2,1)
# plt.subplot(2,1,1)

plt.plot(x_1, f(x_1), color="blue", linewidth=3)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.xlim(-3, 3)
plt.ylim(0, 8)

## Plot 2
plt.subplot(1,2,2)
# plt.subplot(2,1,2)

plt.plot(x_1, df(x_1), color="skyblue", linewidth=5)
plt.xlabel("x", fontsize=12)
plt.ylabel("df(x)", fontsize=12)
plt.xlim(-2, 3)
plt.ylim(-3, 6)
plt.grid()

plt.show()

