class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, data):
        self.filtered_data = list(data.values())[0]
        self.rows = [i for i in self.filtered_data if i["iataCode"] == ""]

    def ok_price(self, data):
        new_data = []
        for i in self.filtered_data:
            if int(i["lowestPrice"]) >= int(data[i["city"]]["price"]):
                new_data.append(
                    {
                        "lowestPrice": i["lowestPrice"],
                        "flight_data": data[i["city"]],
                        "is_ok": True,
                    }
                )
            else:
                new_data.append(
                    {
                        "lowestPrice": i["lowestPrice"],
                        "flight_data": data[i["city"]],
                        "is_ok": False,
                    }
                )
        return new_data
