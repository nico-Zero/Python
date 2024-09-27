import numpy as np
import matplotlib.pyplot as plt
from function import *
from mpl_toolkits.mplot3d.axes3d import Axes3D  # type: ignore
from matplotlib import cm  # ColorMap
from sympy import symbols
from pprint import pprint


def main():
    ab = symbols("x, y")
    print("Our Cost Function:- ", x_y(ab[0], ab[1]))
    cost_ex = x_y(ab[0], ab[1]).evalf(subs={ab[0]: 1.8, ab[1]: 1.0})
    print("Cost at a:1.8 and b:1.0 :- ", cost_ex)
    partial_diff = diff(x_y(ab[0], ab[1]), ab[0])
    print("The partial Derivative:- ", partial_diff)
    diff_cost_ex = diff(x_y(ab[0], ab[1]), ab[0]).evalf(subs={ab[0]: 1.8, ab[1]: 1.0})
    print("Cost of Partial Derivative when a:1.8 and b:1.0 :- ", diff_cost_ex)

    # Batch Gradient Descent with Sympy.
    multiplayer = 0.1
    max_iter = 200
    params = np.array([2.0, 1.0])  # inital Guess
    result = batch_gradient_descent_1(
        func=x_y,
        params=params,
        multiplayer=multiplayer,
        max_iter=max_iter,
    )
    grad_x = result["gradient_arr"][:, 0]
    grad_y = result["gradient_arr"][:, 1]

    print("\nResult:- ")
    pprint(result, indent=4)

    # result = batch_gradient_descent(
    #     func=x_y,
    #     diff_syboles=ab,
    #     params=params,
    #     multiplayer=multiplayer,
    #     max_iter=max_iter,
    # )
    # print("\nResult:- ")
    # pprint(result, indent=4)

    # Plotting the 3d Plot.
    x = np.linspace(-2, 2, 200)
    y = np.linspace(-2, 2, 200)
    x, y = np.meshgrid(x, y)

    fig = plt.figure(figsize=(16, 12))
    ax = fig.add_subplot(projection="3d")
    ax.set_xlabel("X", fontsize=20)
    ax.set_ylabel("Y", fontsize=20)
    ax.set_zlabel("(f(x, y) - Cost)", fontsize=20)  # type: ignore
    ax.plot_surface(x, y, x_y(x, y), cmap=cm.coolwarm, alpha=0.6)  # type: ignore
    ax.scatter(grad_x, grad_y, x_y(grad_x, grad_y), color="red", s=50)  # type: ignore

    # Showing the plot.
    plt.show()


main()
