"""This module contains the Item and Perishables Classes"""

from datetime import date


class Item:
    def __init__(self, name, item_id, warehouse=None):
        """Item Constructor"""
        self._name = name
        self._item_id = item_id
        self._warehouse = warehouse

        # Automatically associate this item with the given warehouse
        if warehouse:
            warehouse.add_item(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        self._item_id = item_id

    @property
    def warehouse(self):
        return self._warehouse

    @warehouse.setter
    def warehouse(self, warehouse):
        self._warehouse = warehouse

    def __repr__(self):
        """Return a string representation of the item for printing"""
        return f"Item {self._name} (ID: {self._item_id})"


class Perishables(Item):
    def __init__(self, name, item_id, expiration_date, warehouse=None):
        """Perishable Constructor"""
        # Call the parent constructor
        super().__init__(name, item_id, warehouse)
        
        # Add expiration_date attribute
        self._expiration_date = expiration_date

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        self._expiration_date = expiration_date

    def is_expired(self):
        """Check if the item is expired by comparing the expiration date to today's date"""
        today = date.today()
        return self._expiration_date < today

    def __repr__(self):
        """Override the string representation to include expiration date and warehouse"""
        warehouse_info = f", Warehouse: {self._warehouse}" if self._warehouse else ""
        return f"Perishable Item {self._name} (ID: {self._item_id}), Expiration Date: {self._expiration_date}{warehouse_info}"
