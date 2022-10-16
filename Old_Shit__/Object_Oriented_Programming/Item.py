import csv
from csv import DictReader as read


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount

    all_item = []

    @staticmethod
    def all():
        print(*Item.all_item, sep="\n")

    def __init__(self, name: str, price: int, quantity: int = 0):

        # Run validations to the received arguments
        if price == str(price) and quantity == str(quantity):
            price = float(price)
            quantity = float(quantity)
        else:
            assert price >= 0 and price == float(
                price
            ), f"Price {price} is not greater then or equal to zero!"
            assert quantity >= 0 and quantity == float(
                quantity
            ), f"Quantity {quantity}, is not greater then or equal to zero!"
        # Assign to self object

        self.__name = name  # __ makes the attribute private.
        self.__price = price
        self.quantity = quantity
        Item.all_item.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self, dis: float = 80):
        self.__price = self.__price - (self.__price / 100 * dis)

    def apply_increment(self, num: float):
        self.__price = self.__price + self.__price * (num / 100)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_n):
        if len(new_n) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = new_n

    def calculate_total_price(self):
        return self.__price * self.quantity

    def __connect(self):
        pass
    def __preapare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regaeds, nico_Zero
        """
    def __send(self):
        pass
    def send_email(self):
        self.__connect
        self.__preapare_body
        self.__send

    @classmethod
    def instantiate_from_csv(cls):
        with open(
            "/media/zero/Software/__/Python/Object_Oriented_Programming/Item.csv", "r"
        ) as f:
            items = list(read(f))

        for item in items:
            Item(
                name=item.get("name"),
                price=item.get("price"),
                quantity=item.get("quantity"),
            )

    @staticmethod
    def is_int(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__} = Name : {self.name}, Price : {self.price}, Quantity : {self.quantity}"
