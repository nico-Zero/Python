from Item import Item

class Phone(Item):

    def __init__(self,name: str,price: int,quantity: int = 0, broken_phones : int = 0):
        
        # Call the super function to have access to all attributes / methods
        super().__init__(
            name,price,quantity
        )
        # Run validations to the received arguments
        if broken_phones == str(broken_phones):
            broken_phones = int(broken_phones)
        else:
            assert broken_phones >=0 and broken_phones == float(broken_phones) ,f"Broken Phones  {broken_phones} is not greater then or equal to zero!"
        # Assign to self object
        
        self.broken_phones = broken_phones
        