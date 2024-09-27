from math import e, log

import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sympy import Symbol, diff, symbols

# CRIM - per capita crime rate by town
# ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
# INDUS - proportion of non-retail business acres per town.
# CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
# NOX - nitric oxides concentration (parts per 10 million)
# RM - average number of rooms per dwelling
# AGE - proportion of owner-occupied units built prior to 1940
# DIS - weighted distances to five Boston employment centres
# RAD - index of accessibility to radial highways
# TAX - full-value property-tax rate per 10,000 dollars
# PTRATIO - pupil-teacher ratio by town
# B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
# LSTAT - % lower status of the population
# PRICES - Median value of owner-occupied homes in 1000 dollars's


# g(x)= x^4 - 4*x^2 + 5
def g(x):
    return (x**4) - (4 * x**2) + (5)


# dg(x)= 3*x - 4*x
def dg(x):
    return (4 * x**3) - (8 * x)


# h(x)= x**5 - 2*x**4 + 2
def h(x):
    return (x**5) - (2 * x**4) + (2)


# dg(x)= 5*x**4 - 8*x**3
def dh(x):
    return (5 * x**4) - (8 * x**3)


def x_y(x, y):
    r = 3 ** ((-(x**2)) - (y**2))
    return 1 / (r + 1)


def dx_y(x, y):
    r = 3 ** ((-(x**2)) - (y**2))
    return 1 / (r + 1)


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


def batch_gradient_descent(
    func,
    diff_syboles: list,
    params,
    multiplayer=0.01,
    max_iter=500,
):
    partial_diff_x = diff(func(*diff_syboles), diff_syboles[0])
    partial_diff_y = diff(func(*diff_syboles), diff_syboles[1])
    gradient_x = partial_diff_x.evalf(
        subs={diff_syboles[0]: params[0], diff_syboles[1]: params[1]}
    )
    gradient_y = partial_diff_y.evalf(
        subs={diff_syboles[0]: params[0], diff_syboles[1]: params[1]}
    )
    gradients = np.array([gradient_x, gradient_y])
    gradient_arr = params.reshape(1, 2)

    for _ in range(max_iter):
        params = params - (multiplayer * gradients)
        gradient_x = partial_diff_x.evalf(
            subs={diff_syboles[0]: params[0], diff_syboles[1]: params[1]}
        )
        gradient_y = partial_diff_y.evalf(
            subs={diff_syboles[0]: params[0], diff_syboles[1]: params[1]}
        )
        gradients = np.array([gradient_x, gradient_y])
        gradient_arr = np.append(arr=gradient_arr, values=params.reshape(1, 2), axis=0)

    return {
        "Gradient": gradients,
        "min_x": params[0],
        "min_y": params[1],
        "min_Cost": func(params[0], params[1]),
        "gradient_arr": gradient_arr,
    }


def fpx(x, y):
    r = 3 ** (-(x**2) - y**2)
    n = 2 * x * log(3) * r
    d = (r + 1) ** 2
    return n / d


def fpy(x, y):
    r = 3 ** (-(x**2) - y**2)
    n = 2 * y * log(3) * r
    d = (r + 1) ** 2
    return n / d


def batch_gradient_descent_1(
    func,
    x_func,
    y_func,
    params,
    multiplayer=0.01,
    max_iter=500,
):
    gradient_x = x_func(params[0], params[1])
    gradient_y = y_func(params[0], params[1])
    gradients = np.array([gradient_x, gradient_y])
    gradient_arr = params.reshape(1, 2)

    for _ in range(max_iter):
        params = params - (multiplayer * gradients)
        gradient_x = x_func(params[0], params[1])
        gradient_y = y_func(params[0], params[1])
        gradients = np.array([gradient_x, gradient_y])
        gradient_arr = np.append(arr=gradient_arr, values=params.reshape(1, 2), axis=0)

    return {
        "Gradient": gradients,
        "min_x": params[0],
        "min_y": params[1],
        "min_Cost": func(params[0], params[1]),
        "gradient_arr": gradient_arr,
    }


def mse(y, y_hat):
    result = (((y - y_hat) ** 2).sum()) / len(y)
    return result


def data_fitting(features, fit_on):
    x_train, x_test, y_train, y_test = train_test_split(
        features, fit_on, test_size=0.2, random_state=10
    )
    x_train = sm.add_constant(x_train)
    x_test = sm.add_constant(x_test)
    traning_model = sm.OLS(y_train, x_train)
    testing_model = sm.OLS(y_test, x_test)
    result = {
        "training": traning_model.fit(),
        "testing": testing_model.fit(),
    }
    return result
