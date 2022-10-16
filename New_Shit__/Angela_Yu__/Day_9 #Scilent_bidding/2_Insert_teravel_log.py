travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]


def add_log(country, visits, cities):
    travel_log.append(
        {
            "country": country,
            "visits": visits,
            "cities": cities,
        }
    )


country = input("Enter the country name: ")
visits = int(input("Enter the numbers of visits: "))
cities = input("Enter the cities: ").split(",")
add_log(country, visits, cities)
print(*travel_log,sep="\n")
