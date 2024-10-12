import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-2.5, 2.5, 1000)

# g(x)= x^4 - 4*x^2 + 5
def g(x):
    return  ( x**4 ) - ( 4*x**2 ) + ( 5 )

# dg(x)= 3*x - 4*x
def dg(x):
    return ( 4*x**3 ) - ( 8*x )

# h(x)= x**5 - 2*x**4 + 2
def h(x):
    return ( x**5 ) - ( 2*x**4 ) + ( 2 )

# dg(x)= 5*x**4 - 8*x**3
def dh(x):
    return ( 5*x**4 ) - ( 8*x**3 )

def gradient_desent(f, df, inital_guess:float=0, min_value:float=0, learning_rate:float=0.1, preciseness:float=0.00001, max_iter=1000):
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
                learning_rate -= ( learning_rate/100 )*50
            # elif dif > last_guess:
            #     learning_rate += ( learning_rate/100 )*50

            x_list.append(inital_guess)
            cost_list.append( f_inital_guess )
            slope_list.append( df_inital_guess )

            last_guess = inital_guess
            if dif < preciseness:
                break
    except OverflowError:
        print("OverFlowError!")
    return (inital_guess, x_list, cost_list, slope_list)

n = 300
local_min_1, list_x_1, cost_list_1, drivative_x_1= gradient_desent(g, dg, inital_guess=3, learning_rate=0.0005, preciseness=0.0001, max_iter=n)
local_min_2, list_x_2, cost_list_2, drivative_x_2= gradient_desent(g, dg, inital_guess=3, learning_rate=0.001, preciseness=0.0001, max_iter=n)
local_min_3, list_x_3, cost_list_3, drivative_x_3= gradient_desent(g, dg, inital_guess=3, learning_rate=0.002, preciseness=0.0001, max_iter=n)
local_min_4, list_x_4, cost_list_4, drivative_x_4= gradient_desent(g, dg, inital_guess=1.9, learning_rate=0.25, preciseness=0.0001, max_iter=n)

# print("Local Min:- ", local_min)
print("Length of list_x_1:- ", len(list_x_1))
print("Length of list_x_2:- ", len(list_x_2))
print("Length of list_x_3:- ", len(list_x_3))
print("Length of list_x_4:- ", len(list_x_4))
# print("List X:- ", list_x)
# print("Cost List", cost_list)

iteration_range_1 = list(range(len(cost_list_1)))
iteration_range_2 = list(range(len(cost_list_2)))
iteration_range_3 = list(range(len(cost_list_3)))
iteration_range_4 = list(range(len(cost_list_4)))

plt.figure(figsize=(20, 10))

# Plotting reduction in cost of each iteration.
plt.title("Effect of the learning rate")
plt.xlabel("No. of iteration")
plt.ylabel("Cost")
plt.xlim(0, len(cost_list_1)+10)
plt.ylim(0, 50)
plt.plot(iteration_range_1 , cost_list_1, color="blue", linewidth=2)
plt.scatter(iteration_range_1, cost_list_1, color="blue", alpha=0.8)

plt.plot(iteration_range_2 , cost_list_2, color="green", linewidth=2)
plt.scatter(iteration_range_2, cost_list_2, color="green", alpha=0.8)

plt.plot(iteration_range_3 , cost_list_3, color="black", linewidth=2)
plt.scatter(iteration_range_3, cost_list_3, color="black", alpha=0.8)

plt.plot(iteration_range_4 , cost_list_4, color="hotpink", linewidth=2)
plt.scatter(iteration_range_4, cost_list_4, color="hotpink", alpha=0.8)

# Showing the plot.
plt.show()


