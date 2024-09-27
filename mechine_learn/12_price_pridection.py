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
# MEDV - Median value of owner-occupied homes in 1000 dollars's

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("./boston.csv")
<<<<<<< HEAD
=======
data.describe()
>>>>>>> 5e99c8e (.)
# data["CHAS"].value_counts()

# data.min()
# data.max()

# data.describe()

# data["MEDV"].corr(data["RM"])
# data["MEDV"].corr(data["PTRATIO"])
# data.corr()  # Pearson corelation cofficent

# mask = np.zeros_like(data.corr())
# triangle_indecis = np.triu_indices_from(mask)
# mask[triangle_indecis] = True
# sns.heatmap(data.corr(), mask=mask, annot=True, annot_kws={"size": 14})
# sns.set_style("white")
# plt.show()

# nox_dis_corr = round(data["NOX"].corr(data["DIS"]), 5)
# plt.scatter(x=data["DIS"], y=data["NOX"], alpha=0.5)
# plt.title(f"NOX vs DIS [corr: {nox_dis_corr}].", fontsize=14)
# plt.xlabel("DIS - weighted distances to 5 Boston employment center.", fontsize=14)
# plt.ylabel("NOX - Nitric Oxides concentration (parts per 10 million)", fontsize=14)
# plt.show()

# sns.set_style("white")
# sns.jointplot(x=data["DIS"], y=data["NOX"], kind="reg", color="Indigo")
# plt.show()

# sns.set_style("white")
# /sns.jointplot(x=data["TAX"], y=data["RAD"], kind="reg", color="Indigo")
# plt.show()

# sns.set_style("white")
# sns.jointplot(x=data["RM"], y=data["MEDV"], kind="reg", color="Indigo")
# plt.show()

# sns.lmplot(x="TAX", y="RAD", data=data)
# plt.show()

# plt.imshow(data.corr())
# plt.show()

# sns.pairplot(data)
# plt.savefig("scatter_pairplot.png")

sns.pairplot(data, kind="reg", plot_kws={"line_kws": {"color": "Indigo"}})
plt.savefig("reg_pairplot.png")

# BIC value of a Model with INDUS value in it and one without it.
