import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# training and test dataset split.
data = pd.read_csv("boston.csv")
prices = data["PRICES"]
features = data.drop("PRICES", axis=1)

# Multivariable regration.
# x_train, x_test, y_train, y_test = train_test_split(
#     features, prices, test_size=0.2, random_state=10
# )

# print(prices)
# print(data)
# print("X_Train:- ", x_train)
# print("X_Test:- ", x_test)
# print("Y_Train:- ", y_train)
# print("Y_Test:- ", y_test)

# regr = LinearRegression()
# regr.fit(x_train, y_train)

# print("Intercept:- ", regr.intercept_)
# # pd.DataFrame(data=regr.coef_, index=x_train.columns, columns=["Coef"])  # type: ignore
# print("r-Squired of Training Dataset:- ", regr.score(x_train, y_train))
# print("r-Squired of Testing Dataset:- ", regr.score(x_test, y_test))

# Data Transformation.
p = data["PRICES"]
lp = np.log(data["PRICES"])

# p, lp
# print(p.skew())
# print(lp.skew())
# sns.distplot(lp)
# plt.title(f"Log Prices with skey{lp.skew()}")
# plt.show()

# transformed_data = features
# transformed_data["LOG_PRICES"] = lp
# # sns.lmplot(
# #     x="LSTAT",
# #     y="LOG_PRICES",
# #     data=transformed_data,
# #     scatter_kws={"alpha": 0.6},
# #     line_kws={"color": "Indigo"},

# running data with log price values.
x_train, x_test, y_train, y_test = train_test_split(
    features, lp, test_size=0.2, random_state=10
)
regr = LinearRegression()
regr.fit(x_train, y_train)
print("Intercept:- ", regr.intercept_)
print("r-Squired of Training Dataset:- ", regr.score(x_train, y_train))
print("r-Squired of Testing Dataset:- ", regr.score(x_test, y_test))
cofe = pd.DataFrame(data=regr.coef_, index=x_train.columns, columns=["Coef"])  # type: ignore
np.e**cofe
