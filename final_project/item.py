"""This module contains the Item and Perishables Classes"""

from datetime import date


class Item:
    def __init__(self, name, item_id, warehouse=None):
        """Item Constructor"""
        self.name = name
        self.item_id = item_id
        self.warehouse = warehouse

        # Automatically associate this item with the given warehouse
        if warehouse:
            warehouse.add_item(self)

    def __repr__(self):
        """Return a string representation of the item for printing"""
        return f"Item {self.name} (ID: {self.item_id})"


class Perishables(Item):
    def __init__(self, name, item_id, expiration_date, warehouse=None):
        """Perishable Constructor"""
        # Call the parent constructor
        super().__init__(name, item_id, warehouse)
        
        # Add expiration_date attribute
        self.expiration_date = expiration_date

    def is_expired(self):
        """Check if the item is expired by comparing the expiration date to today's date"""
        today = date.today()
        return self.expiration_date < today

    def __repr__(self):
        """Override the string representation to include expiration date and warehouse"""
        warehouse_info = f", Warehouse: {self.warehouse}" if self.warehouse else ""
        return f"Perishable Item {self.name} (ID: {self.item_id}), Expiration Date: {self.expiration_date}{warehouse_info}"
