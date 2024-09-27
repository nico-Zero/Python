from logging import exception
import smtplib
from tkinter import *

sender = "zandaxheart955@gmail.com"
receiver = "yuvrajmahilange955@gmail.com"
password = "zandaXheart69"
subject = "Just Wanted."
body = ""

def window():
    def Save():
        global body
        body = body_w.get(1.0,END)
        w.destroy()

    w = Tk()

    title = Label(w,text="Write the body of your email.")
    title.pack()
    body_w = Text(w,width=50,height=20)
    body_w.pack()
    save = Button(w,text="Save",command=Save)
    save.pack()

    w.mainloop()

def Mes_():
    # Header
    global message
    message = f"""From: {sender}
    To: {receiver}
    Subject: {subject}\n
    {body}
    """
window()
Mes_()
# try:    
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender,password)
print("Logged in... :)")
server.sendmail(sender,receiver,message)
print("Email has been sent!")
# except Exception as e:
#     print(f"Error: {e}")
