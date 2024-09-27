import numpy as np
from function import *


def main():
    x = np.array([[0.1, 1.2, 2.4, 3.2, 4.1, 5.7, 6.5]]).transpose()
    y = np.array([1.7, 2.4, 3.5, 3.0, 6.1, 9.4, 8.2]).reshape(7, 1)
    nr_thetas = 200
    th_0 = np.linspace(start=-1, stop=3, num=nr_thetas)
    th_1 = np.linspace(start=-1, stop=3, num=nr_thetas)
    plot_0, plot_1 = np.meshgrid(th_0, th_1)
    plot_cost = np.zeros((nr_thetas, nr_thetas))  # type: ignore
    for i in range(nr_thetas):
        for j in range(nr_thetas):
            y_hat = plot_0[i][j] + plot_1[i][j] * x
            plot_cost[i][j] = mse(y, y_hat)
    print("min cost:- ", plot_cost.min())
    i, j = np.unravel_index(indices=plot_cost.argmin(), shape=plot_cost.shape)
    print("i,j are:- ", (i, j))
    print(f"Min MSE for Theta 0 at plot_0[{i}][{j}]", plot_0[i][j])
    print(f"Min MSE for Theta 1 at plot_1[{i}][{j}]", plot_1[i][j])


main()
