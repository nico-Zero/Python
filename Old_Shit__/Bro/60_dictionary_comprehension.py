cities_in_F  = {
    "New York": 32,
    "Boston": 75,
    "Los Angeles": 100,
    "Chicago": 50
}

cities_in_C = {key : round((value-32)*5/9) for (key,value) in cities_in_F.items()}
print(cities_in_C)

weather = {
    "New York": "snowing",
    "Boston": "sunny",
    "Los Angeles": "sunny",
    "Chicago": "cloudy"
}
sunny = {key : value for (key,value) in weather.items() if value == "sunny"}
snowing = {key : value for (key,value) in weather.items() if value == "snowing"}
cloudy = {key : value for (key,value) in weather.items() if value == "cloudy"}

print(sunny)
print(snowing)
print(cloudy)

iscold = {key : ("COLD" if value <= 40 else "WARM") for (key,value) in cities_in_F.items() }
print(iscold)

def check_temp(x):
    if x >= 70:
        return "HOT"
    elif 69 >= x >= 40 >= 60:
        return 'WARM'
    else:
        return "COLD"

check = {key : check_temp(value) for (key,value) in cities_in_F.items() }
print(check)

