import numpy as np
import matplotlib.pyplot as plt
from function import *  # type: ignore
from mpl_toolkits.mplot3d.axes3d import Axes3D  # type: ignore
from matplotlib import cm  # ColorMap

x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)

x, y = np.meshgrid(x, y)

print(x, y)


def gradient_desent(
    f,
    df,
    inital_guess: float = 0,
    min_value: float = 0,
    learning_rate: float = 0.1,
    preciseness: float = 0.00001,
    max_iter=1000,
):
    x_list = [inital_guess]
    cost_list = [f(inital_guess)]
    slope_list = [df(inital_guess)]
    last_guess = inital_guess
    try:
        for _ in range(max_iter):
            min_value = inital_guess
            gradient = df(min_value)
            inital_guess = min_value - (learning_rate * gradient)
            f_inital_guess = f(inital_guess)
            df_inital_guess = df(inital_guess)
            dif = abs(inital_guess - min_value)
            if dif < last_guess:
                learning_rate -= (learning_rate / 100) * 50
            # elif dif > last_guess:
            #     learning_rate += ( learning_rate/100 )*50

            x_list.append(inital_guess)
            cost_list.append(f_inital_guess)
            slope_list.append(df_inital_guess)

            last_guess = inital_guess
            if dif < preciseness:
                break
    except OverflowError:
        print("OverFlowError!")
    return (inital_guess, x_list, cost_list, slope_list)


fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(projection="3d")

# Plotting the 3d Plot.
ax.set_xlabel("X", fontsize=20)
ax.set_ylabel("Y", fontsize=20)
ax.set_zlabel("(f(x, y) - Cost)", fontsize=20)  # type: ignore

ax.plot_surface(x, y, x_y(x, y), cmap=cm.coolwarm, alpha=0.6)  # type: ignore

# Showing the plot.
plt.show()
