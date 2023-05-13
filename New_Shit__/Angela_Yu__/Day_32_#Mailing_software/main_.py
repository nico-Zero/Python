from datetime import datetime
import smtplib
# from random import choice
from email.message import EmailMessage
import ssl


my_email = "ZandaXheart955@gmail.com"
friend_email = "nicozero674@yahoo.com"
my_pass = "imlhjktowhazcccc"

now = datetime.now()
week_day = now.weekday()


if week_day == 1:
    # with open("New_Shit__/Angela_Yu__/Day_32 #Mailing_software/quotes.txt") as file:
    #     quot = file.readiness()
    #     random_quot = choice(quot)
    #     print(random_quot)

    subject = "GoodMorning"
    body = "random_quot"

    em = EmailMessage()
    em["From"] = my_email
    em["To"] = friend_email
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    # Port for SSL: 465 Port for TLS/STARTTLS: 587
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as connection:
        connection.login(my_email, my_pass)
        connection.sendmail(
            my_email,
            friend_email,
            em.as_string(),
        )
print("done...")
