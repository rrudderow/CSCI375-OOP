#! usr/bin/env python3

"""
Warehouse Class:
* __init__
* add_item
* send_item
* remove_item
* __print__
"""

from item import Item


class Warehouse:
    def __init__(self, name: str) -> None:
        """ Constructor """
        self._name: str = name
        self._items: Item = []  # should be viable with subclasses of Item

    @property
    def name(self) -> str:
        """ Getter for _name """
        return self._name

    @property
    def items(self) -> list[Item]:
        """ Getter for _items """
        return self._items

    def add_item(self, item: Item) -> None:
        """ Adds an item to the Warehouse """
        self.items.append(item)

    def send_item(self, item_name: str, other: "Warehouse") -> None:
        """ Sends an item from current Warehouse to another """
        item = next((item for item in self.items if item.name == item_name), None)
        if not item:
            raise ValueError(f"Item '{item_name}' not found in {self.name}.")
        other.add_item(item)
        self.remove_item(item_name)

    def remove_item(self, item_name: str) -> None:
        """ Removes an item from the current Warehouse """
        self._items = [item for item in self.items if item.name != item_name]

    def list_items(self):
        """ Prints unique """
        if not self.items:
            print(f"{self.name} is empty.")
        else:
            for item in self.items:
                print(f"{item.name}")
