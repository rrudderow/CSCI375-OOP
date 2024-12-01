"""This module contains the Item and Perishables Classes"""

from typing import List, Any
from observer import Observer


class Subject:
    """Subject Class"""
    def __init__(self) -> None:
        """initialize"""
        self._observers: List["Observer"] = []

    def register_observer(self, observer: "Observer") -> None:
        """Add Observer"""
        self._observers.append(observer)

    def remove_observer(self, observer: "Observer") -> None:
        """Remove Observer"""
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        """Update Observer"""
        for observer in self._observers:
            observer.update()


class Item(Subject):
    """Item CLass"""
    def __init__(self, name: str, item_id: int, price: float,
                 warehouse: Any | None) -> None:
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
    def name(self) -> str:
        """Returns Item name"""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Set Item name"""
        self._name = name

    @property
    def item_id(self) -> int:
        """Returns Item ID"""
        return self._item_id

    @item_id.setter
    def item_id(self, item_id: int) -> None:
        """Set Item ID"""
        self._item_id = item_id

    @property
    def price(self) -> float:
        """Returns Item price"""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Set and Update Item price"""
        if self._price != new_price:
            self._price = new_price
            self.notify_observers()  # Notify observers when the price changes

    @property
    def warehouse(self) -> Any:
        """Return warehouse"""
        return self._warehouse

    @warehouse.setter
    def warehouse(self, warehouse: Any) -> None:
        """Set Item warehouse"""
        self._warehouse = warehouse

    def __repr__(self) -> str:
        """Return a string representation of the item for printing"""
        return f"Item {self._name} (ID: {self._item_id}) Price: ${self._price}"
