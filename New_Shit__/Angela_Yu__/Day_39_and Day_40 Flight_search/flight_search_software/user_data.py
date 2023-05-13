from json import dump
from requests import get, post, put
from faker import Faker
from notification_manager import NotificationManager


class User:
    def __init__(
        self,
        on_data="https://api.sheety.co/396fe2deb7f4f387c77a206b624a1c7e/userData/sheet1",
    ):
        self.data_url = on_data

        ## ----------------------------------------------------------------------------------------GETTING USER DATA'S

        self.the_data = get(url=self.data_url)
        self.the_data.raise_for_status()
        self.the_data = self.the_data.json().get("sheet1")
        self.first_names = [i["firstName"] for i in self.the_data]
        with open("user_data.json", "w") as file:
            dump(self.the_data, file, indent=4)

        while 1:
            self.user_first_name = input("What is your First name:- ")
            if self.user_first_name in self.first_names:
                print("This name is already in database !")
                continue
            else:
                break
        self.user_last_name = input("What is your Last name:- ")
        while 1:
            self.user_password = input("What is your Password:- ")
            check = input("Enter your password again:- ")
            if self.user_password == check:
                break
            else:
                print("Password does not match!")
                continue
        while 1:
            self.user_phone_number = input("Enter your Phone Number:- ")
            otp = Faker().postcode()
            send_otp = NotificationManager().otp(otp, self.user_phone_number)
            print(send_otp)
            check_otp = input("Enter the OTP:- ")
            if otp == check_otp:
                break
            else:
                print("Wrong OTP!")
                continue

        ## ----------------------------------------------------------------------------------------UPLOADING USER DATA'S
        ## ----------------------------------------------------------WRITING NEW USER DATA
        if self.user_first_name not in self.first_names:
            parameters = {
                "sheet1": {
                    "firstName": self.user_first_name,
                    "lastName": self.user_last_name,
                    "phoneNumber":self.user_phone_number,
                    "password": self.user_password,
                }
            }
            self.outgoing_data = post(url=self.data_url, json=parameters)

            ## ---------------------------------------------------------GETTING UPDATED USER DATA
            self.the_data = get(url=self.data_url)
            self.the_data.raise_for_status()
            self.the_data = self.the_data.json().get("sheet1")
            with open("user_data.json", "w") as file:
                dump(self.the_data, file, indent=4)


x = User()

print(x.the_data)
