import smtplib

email = "nico.zero.0x@gmail.com"
our_email = "zandaxheart955@gmail.com"
message = "Hello NicoZero!"


our_email = "zandaxheart955@gmail.com"
message = f"""
From: From Person {email}
To: To Person {our_email}
Subject: Contact By Blog Site
{message}
"""
# try:
password = input("Enter your password:- ")
sending_email = smtplib.SMTP("gmail.com", 587)
sending_email.login(email, password)
sending_email.sendmail(email, our_email, message)
print("Successfully sent email.")
# except:
#     print("Unable to send email.")
