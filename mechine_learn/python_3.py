import pandas as pd
# from pandas import DataFrame

data = pd.read_csv("lsd_math_score_data.csv")

# print(data)
# print(data["Time_Delay_in_Minutes"])
# print(data["LSD_ppm"][0])
only_math_score = data["Avg_Math_Test_Score"]

data["Test_Subject"] = "Jennifer Lopez"
data["High_Score"] = 100

data["High_Score"] = data["High_Score"] + data["Avg_Math_Test_Score"]

data["High_Score"] = data["High_Score"] ** 3

# print(type( data["Avg_Math_Test_Score"] ))

# columnList = {"LSD_ppm": data["LSD_ppm"],"Avg_Math_Test_Score": data["Avg_Math_Test_Score"]}
# dataColumnList = DataFrame(columnList)
#
# print(dataColumnList)

cleanData = data[["LSD_ppm", "Avg_Math_Test_Score"]]

# print(cleanData)
# print(type( cleanData ))

# X = data[ ["LSD_ppm"] ]
# print(type( X ))

print(data)

del data["Test_Subject"]

print(data)

del data["High_Score"]

print(data)
# /run/media/nico/Nova/Lab/Python/mechine_learn

