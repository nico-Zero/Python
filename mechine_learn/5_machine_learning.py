import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2 + x + 1


# make data
x_1 = np.linspace(start=-3, stop=3, num=100)


## Slope & Deritive of Function.
def df(x):
    return 2 * x + 1


# Gradent Desend
new_x = -3
previous_x = 0
step_multiplayer = 0.1
preciseness = 0.00001
x_list = [new_x]
slope_list = [df(new_x)]
for i in range(300):
    previous_x = new_x
    gradient = df(previous_x)
    new_x = previous_x - (step_multiplayer * gradient)
    x_list += [new_x]
    slope_list += [df(new_x)]
    if abs(new_x - previous_x) < preciseness:
        break
print("Local minimal occers at: ", new_x)
print("Slope or df(x) at this point: ", df(new_x))
print("f(x) value of cost: ", f(new_x))
print(x_list)
print(slope_list)

## Plot Function and deritive side by side.
plt.figure(figsize=(15, 5))

# Chart 1: Normal
plt.subplot(3, 1, 1)
plt.plot(x_1, f(x_1), color="blue", linewidth=3)
plt.title("Normal Slope.")
plt.xlim(-3, 3)
plt.ylim(0, 8)
np_x_list = np.array(x_list)
plt.scatter(x_list, f(np_x_list), color="red", s=100, alpha=0.7)

# Chart 3: Drative
plt.subplot(3, 1, 2)
plt.plot(x_1, df(x_1), color="skyblue", linewidth=5)
plt.title("Cost Function.")
plt.xlim(-2, 3)
plt.ylim(-3, 6)
plt.grid()
plt.scatter(x_list, slope_list, color="red", s=100, alpha=0.7)

# Chart 3: Close Up
plt.subplot(3, 1, 3)
plt.plot(x_1, df(x_1), color="skyblue", linewidth=5)
plt.title("Gradiant Desant Close Up.")
plt.xlim(-0.55, -0.2)
plt.ylim(-0.3, 0.8)
plt.grid()
plt.scatter(x_list, slope_list, color="red", s=100, alpha=0.7)

# Finally showing the plot.
plt.show()
