from requests import get, post, put
from json import dump


class User:
    def __init__(
        self,
        first_name=None,
        last_name=None,
        password=None,
        on_data="https://api.sheety.co/396fe2deb7f4f387c77a206b624a1c7e/userData/sheet1",
    ):

        self.user_first_name = first_name or input("What is your First name:- ")
        self.user_last_name = last_name or input("What is your Last name:- ")
        self.user_password = password or input("What is your Password:- ")
        # self.user_data = input("Enter your data:- ")
        self.data_url = on_data

        # ----------------------------------------------------------------------------------------GETTING USER DATA'S
        self.the_data = get(url=self.data_url)
        self.the_data.raise_for_status()
        self.the_data = self.the_data.json().get("sheet1")

        with open("user_data.json", "w") as file:
            dump(self.the_data, file, indent=4)

        # ----------------------------------------------------------------------------------------UPLOADING USER DATA'S

        parameters = {
            "sheet1": {
                "firstname": self.user_first_name,
                "lastname": self.user_last_name,
                "userid": self.user_password,
            }
        }

        self.outgoing_data = post(url=self.data_url, json=parameters)


x = User(first_name="zanda", last_name="nova", password="fuck")

print(x.the_data)
