#! usr/bin/env python3

"""
Warehouse Class:
* __init__
* add_item
* remove_item
* __repr__
"""

from typing import Dict
from item import Item
from perishables import Perishables


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
        # This functionality should be moved to the Warehouses class
        item = next((item for item in self.items if item.name == item_name), None)
        if not item:
            raise ValueError(f"Item '{item_name}' not found in {self.name}.")
        other.add_item(item)
        self.remove_item(item_name)

    def remove_item(self, item_name: str) -> None:
        """ Removes an item from the current Warehouse """
        self.items.remove(next((item for item in self.items if item.name == item_name), None))

    def list_items(self):
        """ Prints unique """
        # I'm only keeping this function to work with main.py's syntax
        # you should just be able to use print(repr(<warehouse>))
        # I'll delete this when we're only using Warehouses and the CLI
        print("Warehouse.list_items() called!")
        print(self)

    def __repr__(self) -> str:
        """ Uses an iterator to create string repr of the Warehouse """
        output: str = f"{self.name}:\n"
        item_counts: Dict[str, int] = {}
        if len(self.items) == 0:
            output = output + "| This warehouse is empty.\n"
            return output

        it = iter(self.items)
        while True:
            try:
                item = next(it)
            except StopIteration:
                break
            else:  # main path
                # output = output + "| " + repr(item) + ". Count: {}."
                if repr(item) not in item_counts:
                    item_counts[repr(item)] = 1
                else:
                    item_counts[repr(item)] += 1

        for key, value in item_counts.items():
            output += f"| {key}; Count: {value}\n"

        return output
