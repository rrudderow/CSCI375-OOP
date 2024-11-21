"""This module contains the Item and Perishables Classes"""

from datetime import date


class Item:
    def __init__(self, name: str, item_id: int, warehouse: str) -> None:
        """Item Constructor"""
        self._name = name
        self._item_id = item_id
        self._warehouse = warehouse
        warehouse.add_item(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def item_id(self) -> int:
        return self._item_id

    @item_id.setter
    def item_id(self, item_id: int) -> None:
        self._item_id = item_id

    @property
    def warehouse(self) -> str:
        return self._warehouse

    @warehouse.setter
    def warehouse(self, warehouse: str) -> None:
        self._warehouse = warehouse

    def __repr__(self) -> str:
        """Return a string representation of the item for printing"""
        return f"Item {self._name} (ID: {self._item_id})"
