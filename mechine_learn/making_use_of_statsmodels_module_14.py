import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from pprint import pprint
from function import *

# training and test dataset split.
data = pd.read_csv("boston.csv")
prices = data["PRICES"]
features = data.drop("PRICES", axis=1)

# Data Transformation.
p = data["PRICES"]
lp = np.log(data["PRICES"])

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
# np.e**cofe

# Using the StatsModels Moule to find the Detailed stats of Data.
x_incl_const = sm.add_constant(x_train)
model = sm.OLS(y_train, x_incl_const)
results = model.fit()
orignal_cofe = pd.DataFrame(
    {"Coef": results.params, "P-Values": round(results.pvalues, 6)}
)
results.rsquared
results.bic

# Testing for Multicollinearity in Boston data.
# vif = [variance_inflation_factor(x_incl_const, i) for i in range(x_incl_const.shape[1])]
# vif = pd.DataFrame({"Conf_Name": x_incl_const.columns, "VIF": np.around(vif, 3)})  # type: ignore
# print(vif)
p = data["PRICES"]
lp = np.log(data["PRICES"])

# residuals and residual plot.
# Using StatsModel.
redused_log = data_fitting(features.drop(["INDUS", "AGE"], axis=1), lp)
normal_values = data_fitting(features, prices)
omitted_values = data_fitting(
    features.drop(["INDUS", "AGE", "LSTAT", "RM", "NOX", "CRIM"], axis=1), lp
)

# graph of actual and pridected values.
# corr = y_train.corr(training_result.fittedvalues)  # type: ignore
# plt.scatter(x=y_train, y=training_result.fittedvalues, color="Indigo", alpha=0.5)
# plt.plot(y_train, y_train, color="Red")
# plt.title("Actual and Pridected Log values")
# plt.xlabel("Logged Prices.")
# plt.ylabel("Fitted values.")
# plt.show()

# plt.scatter(x=np.e**y_train, y=np.e**training_result.fittedvalues, color="Indigo", alpha=0.5)  # type: ignore
# plt.plot(np.e**y_train, np.e**y_train, color="Red")  # type: ignore
# plt.title("Actual and Pridected Log values.")
# plt.xlabel("House Prices in 1000 Dollers.")
# plt.ylabel("Fitted values.")
# plt.show()

# plt.scatter(x=training_result.fittedvalues, y=training_result.resid, color="Indigo", alpha=0.5)  # type: ignore
# # plt.plot(np.e**y_train, np.e**y_train, color="Red")  # type: ignore
# plt.title("Actual and Pridected Log values.")
# plt.xlabel("House Prices in 1000 Dollers.")
# plt.ylabel("Fitted values.")
# resid_mean = round(training_result.resid.mean(), 3)
# resid_skew = round(training_result.resid.skew(), 3)
# plt.show()

# sns.distplot(training_result.resid, color="Indigo")
# plt.show()

redused_log_mse = round(redused_log["training"].mse_resid, 3)
redused_log_rsquared = round(redused_log["training"].rsquared, 3)
redused_log_rmse = round(np.sqrt(redused_log["training"].mse_resid), 3)
normal_values_mse = round(normal_values["training"].mse_resid, 3)
normal_values_rsquared = round(normal_values["training"].rsquared, 3)
normal_values_rmse = round(np.sqrt(normal_values["training"].mse_resid), 3)
omitted_values_mse = round(omitted_values["training"].mse_resid, 3)
omitted_values_rsquared = round(omitted_values["training"].rsquared, 3)
omitted_values_rmse = round(np.sqrt(omitted_values["training"].mse_resid), 3)
the_dataframe = pd.DataFrame(
    {
        "MSE": [
            redused_log_mse,
            normal_values_mse,
            omitted_values_mse,
        ],
        "R_Squared": [
            redused_log_rsquared,
            normal_values_rsquared,
            omitted_values_rsquared,
        ],
        "RMSE": [
            redused_log_rmse,
            normal_values_rmse,
            omitted_values_rmse,
        ],
    }
)
print(the_dataframe)
