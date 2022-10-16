from Item import Item

class Keyboard(Item):

    def __init__(self,name: str,price: int,quantity: int = 0):
        
        # Call the super function to have access to all attributes / methods
        super().__init__(
            name,price,quantity
        )

        