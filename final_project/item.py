"""This module contains the Item and Perishables Classes"""

from datetime import date
from typing import List
from observer import Observer

class Subject:
    def __init__(self):
        self._observers: List["Observer"] = []

    def register_observer(self, observer: "Observer"):
        self._observers.append(observer)

    def remove_observer(self, observer: "Observer"):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

class Item(Subject):
    def __init__(self, name: str, item_id: int, price: float, warehouse=None) -> None:
        """Item Constructor"""
        super().__init__()
        self._name = name
        self._item_id = item_id
        self._price = price
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
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price: float):
        if self._price != new_price:
            self._price = new_price
            self.notify_observers()  # Notify observers when the price changes

    @property
    def warehouse(self):
        return self._warehouse

    @warehouse.setter
    def warehouse(self, warehouse):
        self._warehouse = warehouse

    def __repr__(self):
        """Return a string representation of the item for printing"""
        return f"Item {self._name} (ID: {self._item_id}) Price: ${self._price}"
