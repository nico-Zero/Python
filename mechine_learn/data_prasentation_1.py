import matplotlib.pyplot as plot
import pandas
from pandas import DataFrame
from sklearn.linear_model import LinearRegression

cost_data = pandas.read_csv("cost_revenue_clean_1.csv")

# X = cost_data["Production_Budget"]
# Y = cost_data["Worldwide_Gross"]

X = DataFrame(cost_data, columns=["Production_Budget"])
Y = DataFrame(cost_data, columns=["Worldwide_Gross"])

plot.figure(figsize=(10,6))
plot.scatter(X,Y, alpha=0.3)
plot.title("Budget Report")
plot.xlim(0,450000000)
plot.ylim(0,3000000000)
# plot.show()

regression = LinearRegression()
regression.fit(X, Y)

print(regression.coef_)
print(regression.intercept_)
