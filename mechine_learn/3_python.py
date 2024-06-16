import pandas as pd

data = pd.read_csv("lsd_math_score_data.csv")

# print(data)
# print(data["Time_Delay_in_Minutes"])
# print(data["LSD_ppm"][0])
Avg_Math_Test_Score = data["Avg_Math_Test_Score"]
print(Avg_Math_Test_Score)

