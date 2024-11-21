from item import Item
from datetime import date

class Perishables(Item):
    def __init__(self, name: str, item_id: int, expiration_date: date, warehouse: str) -> None:
        """Perishable Constructor"""
        # Call the parent constructor
        super().__init__(name, item_id, warehouse)
        
        # Add expiration_date attribute
        self._expiration_date = expiration_date

    @property
    def expiration_date(self) -> date:
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date) -> None:
        self._expiration_date = expiration_date

    def is_expired(self) -> bool:
        """Check if the item is expired by comparing the expiration date to today's date"""
        today = date.today()
        return self._expiration_date < today

    def __repr__(self) -> str:
        """Override the string representation to include expiration date and warehouse"""
        warehouse_info = f", Warehouse: {self._warehouse}" if self._warehouse else ""
        return f"Perishable Item {self._name} (ID: {self._item_id}), Expiration Date: {self._expiration_date}{warehouse_info}"
