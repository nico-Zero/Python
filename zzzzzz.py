from email.message import EmailMessage
import smtplib
import ssl

our_email = "zandaxheart955@gmail.com"
password = "slemixowrmjmezyt"

email = "nico.zero.0x@gmail.com"

subject = "Contact By Blog Site"
message = "Hello NicoZero!"


em = EmailMessage()
em["From"] = our_email
em["To"] = email
em["subject"] = subject
em.set_content(message)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(our_email, password)
    smtp.sendmail(our_email, email, em.as_string())

print("successfully sent👌👌")