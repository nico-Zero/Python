from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(
        self,
        twilio_account_sid="AC07a81f1226651d58932b3890f2aa5e65",
        twilio_auth_token="606344a8e18280136fc06755e7489eec",
    ) -> None:
        self.client = Client(twilio_account_sid, twilio_auth_token)

    def send_message(self, data: list):
        status = []
        for i in data:
            city = i["flight_data"]["cityTo"]
            price = i["lowestPrice"]
            message = f"Trip to {city}, The price is {price}"

            if i["is_ok"] == True:
                self.message = self.client.messages.create(
                    body=message,
                    from_="+12017206236",
                    to="+917247477955",
                )
                status.append(str(self.message.status).capitalize() + " to " + city)
            else:
                status.append("No Flight to " + city)

        return status

    def otp(self, message, to):
        self.message = self.client.messages.create(
            body=message,
            from_="+12017206236",
            to="+91" + str(to),
        )
        return self.message.status
