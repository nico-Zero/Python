import pandas

data = pandas.read_csv("New_Shit__/Angela_Yu__/Day_25 #usa_game/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))


data_dict = data.to_dict()
data_list_temp = data["temp"].to_list()
temp_max = max(data_list_temp)
data_max_temp = data[data.temp == temp_max]


def farh(cel):
    return (cel * (9 / 5)) + 32


# print("Max Temperature:- ", temp_max)
print(data_max_temp)


# day = input("Check the temperature of the day? ")
# day_temp = data[data.day == day]

# print(f"\ntemp in {day}", farh(*day_temp.temp.to_list()))

# data_dict = {"student": ["Amy", "James", "Angela"], "score": [76, 56, 45]}
# data = pandas.DataFrame(data_dict)

# print(data)
