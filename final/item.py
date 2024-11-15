class Item:
    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        self._item_id = item_id
        self._name = name
        self._quantity = quantity
        self._price = price
    
    def update_quantity(self, amount: int):
        self._quantity += amount

    def __str__(self):
        return f"Item({self._item_id}): {self._name}, Quantity: {self._quantity}, Price: {self._price}"
