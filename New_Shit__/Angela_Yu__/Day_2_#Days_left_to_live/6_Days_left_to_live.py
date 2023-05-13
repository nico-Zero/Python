from email import message


age = int(input("What is your age ? "))

years_left = 90 - age
if age >= 18:
    days = 365 * years_left
    weeks = 52 * years_left
    months = 12 * years_left

    print(f"You have {days} days, {weeks} weeks, anf {months} months left.")
else:
    message ="""
You are too young to know how many days you got left.
Go enjoy your life until you not 18."""

    print(message)
    
