from datetime import datetime
import smtplib
from random import choice
from pandas import read_csv

LETTERS = [
    "New_Shit__/Angela_Yu__/Day_32 #Mailing_software/letter_templates/letter_1.txt",
    "New_Shit__/Angela_Yu__/Day_32 #Mailing_software/letter_templates/letter_2.txt",
    "New_Shit__/Angela_Yu__/Day_32 #Mailing_software/letter_templates/letter_3.txt",
]
my_email = "nicozero674@yahoo.com"
my_pass = "FuckYouIn_69"

today = datetime.now()
today_month = today.month
today_day = today.day

birthdays = read_csv("New_Shit__/Angela_Yu__/Day_32 #Mailing_software/birthdays.csv")
birthdays = birthdays.to_dict(orient="records")
for i in birthdays:
    if i["month"] == today_month and i["day"] == today_day:
        with open(choice(LETTERS)) as file:
            birthday_letter = file.read().replace("[NAME],", i["name"] + ",")
            print(birthday_letter)

        # Port for SSL: 465 Port for TLS/STARTTLS: 587
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=i["email"],
                msg=f"Subject:Happy Birthday {i['name']}\n\n{birthday_letter}",
            )
