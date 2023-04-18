print("Welcome to the tip calculater.")
bill = float(input("What is the total bill ? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_between = int(input("How many people to split the bill ? "))
splited_bill = round((((bill/ 100)* tip_percentage)+ bill)/ split_between, 2)

print(f"Each person should pay: ${splited_bill}")