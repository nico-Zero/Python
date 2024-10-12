import matplotlib.pyplot as plot
from sklearn.linear_model import LinearRegression
import pandas as pd


data = pd.read_csv("other/lsd_math_score_data.csv")

time = data[["Time_Delay_in_Minutes"]]
LSD = data[["LSD_ppm"]]
score = data[["Avg_Math_Test_Score"]]

# plt.plot(time, LSD, color="g")
# plt.xlabel("Time in Minutes")
# plt.ylabel("Tissue LSD ppm")
# plt.title("Wagner et al. (1968)")
#
# plt.show()

regr = LinearRegression()
regr.fit(LSD, score)

coef = regr.coef_
intercept = regr.intercept_
r_square = regr.score(LSD, score)
pridected_score = regr.predict(LSD)

print(f"Thetal:- {coef[0][0]}")
print(f"Intercept:- {intercept[0]}")  # type: ignore
print(f"R-Square:- {r_square}")

plot.figure(figsize=(10, 8))
plot.style.use("fivethirtyeight")
plot.title("Arithmetic vs LSD-25", fontsize=17)
plot.xlabel("Tissue LSD ppm", fontsize=10)
plot.ylabel("Performance Score", fontsize=10)

plot.scatter(LSD, score, color="blue", s=LSD * 70, alpha=0.6)
plot.plot(LSD, pridected_score, color="red", linewidth=3)
plot.show()
