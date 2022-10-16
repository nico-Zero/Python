import pandas

weather_c = {
    "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ],
    "temp": [
        12,
        14,
        15,
        14,
        21,
        22,
        24,
    ],
}


weather_dataframe = pandas.DataFrame(weather_c)

# print(weather_dataframe)

# for (key, value) in weather_dataframe.items():
#     print("\n",key,":- ")
#     print(value)

#Loop through rows of a data frame

for (index, row) in weather_dataframe.iterrows():
    # print(index)
    print(row)
