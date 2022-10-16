month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
    if int(year) % 4 == 0:
        return True
    else:
        return False

def number_of_days(year,month):
    leap = leap_year(year)
    if month == 2 and leap:
        return 29
    else:
        return month_days[month-1]

year = int(input("Enter a year in number: "))
month = int(input("Enter month in 1-12: "))

print(f"Days in month are : {number_of_days(year,month)}")
