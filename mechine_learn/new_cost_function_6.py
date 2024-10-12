import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 1000)

# g(x)= x^4 - 4*x^2 + 5
def g(x):
    return  ( x**4 ) - ( 4*x**2 ) + ( 5 )

# dg(x)= 3*x - 4*x
def dg(x):
    return ( 4*x**3 ) - ( 8*x )

# Gradent Decent
def gradient_desent(f, df, inital_guess:float=0, min_value:float=0, multiplayer:float=0.1, preciseness:float=0.00001, max_iter=500):
    x_list = [inital_guess]
    cost_list = [f(inital_guess)]
    slope_list = [df(inital_guess)]
    try:
        for _ in range(max_iter):
            min_value = inital_guess
            gradient = df(min_value)
            inital_guess = min_value - (multiplayer * gradient)
            f_inital_guess = f(inital_guess)
            df_inital_guess = df(inital_guess)

            x_list.append(inital_guess)
            cost_list.append( f_inital_guess )
            slope_list.append( df_inital_guess )

            if abs(inital_guess - min_value) < preciseness:
                break
    except OverflowError:
        print("OverFlowError!")
    return (inital_guess, x_list, cost_list, slope_list)


local_min, list_x, cost_list, drivative_x = gradient_desent(g, dg, inital_guess=0.2, multiplayer=0.02, preciseness=0.001)

# print("Local Min:- ", local_min)
print("Length of list_x:- ", len(list_x))
# print("List X:- ", list_x)
# print("Cost List", cost_list)

# Plot 1:
plt.subplot(2,1,1)
plt.title("Cost Function")
plt.ylabel("Y")
plt.xlim()
plt.ylim()
plt.plot(x ,g(x), color="blue", linewidth=2)
plt.scatter(list_x, cost_list, color="red", s=100, alpha=0.7)

# Plot 2:
plt.subplot(2,1,2)
plt.title("Slope of Cost Function")
plt.ylabel("Y")
plt.xlim()
plt.ylim()
plt.plot(x ,dg(x), color="skyblue", linewidth=2)
plt.scatter(list_x, drivative_x, color="red", s=100, alpha=0.7)

# Showing the plot.
plt.show()
