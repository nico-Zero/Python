from datetime import datetime
import smtplib
from random import choice

my_email = "nicozero674@yahoo.com"
friend_email = "zandaxheart955@gmail.com"
my_pass = "FuckYouIn_69"

now = datetime.now()
week_day = now.weekday()


if week_day == 0:
    with open("New_Shit__/Angela_Yu__/Day_32 #Mailing_software/quotes.txt") as file:
        quot = file.readlines()
        random_quot = choice(quot)
        print(random_quot)

    # Port for SSL: 465 Port for TLS/STARTTLS: 587
    with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=friend_email,
            msg=f"Subject:Happy GoodMorning\n\n{random_quot}",
        )
