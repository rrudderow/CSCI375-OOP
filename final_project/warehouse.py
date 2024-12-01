#! usr/bin/env python3

"""
Warehouse Class:
* __init__
* add_item
* remove_item
* __repr__
"""

from typing import Dict, List
from item import Item
from perishables import Perishables
from observer import Observer

class Warehouse(Observer):
    def __init__(self, name: str) -> None:
        """ Constructor """
        self._name: str = name
        self._items: List[Item] = []  # should be viable with subclasses of Item

    @property
    def name(self) -> str:
        """ Getter for _name """
        return self._name

    @property
    def items(self) -> List[Item]:
        """ Getter for _items """
        return self._items

    def add_item(self, item: Item) -> None:
        """ Adds an item to the Warehouse """
        item.register_observer(self)
        self.items.append(item)

    def send_item(self, item_name: str, other: "Warehouse") -> None:
        """ Sends an item from current Warehouse to another """
        # This functionality should be moved to the Warehouses class
        item = next((item for item in self.items if item.name == item_name), None)
        if not item:
            raise ValueError(f"Item '{item_name}' not found in {self.name}.")
        other.add_item(item)
        self.remove_item(item_name)

    def remove_item(self, item: Item) -> None:
        """ Removes an item from the current Warehouse """
        item.remove_observer(self)
        self.items.remove(next((item for item in self.items if item.name == item), None))

    def cli_items(self) -> Dict[str, int]:
        """ Prints unique """
        item_counts: Dict[str, int] = {}
        it = iter(self.items)

        while True:
            try:
                item = next(it)
            except StopIteration:
                break
            else:  # main path
                if repr(item) not in item_counts:
                    item_counts[repr(item)] = 1
                else:
                    item_counts[repr(item)] += 1
        return item_counts

    def update(self):
        print(f"{self.name} has been notified about the price change.")

    def update_item_price(self, item_name: str, new_price: float) -> None:
        """Finds an item by its name and updates its price."""
        item = next((item for item in self.items if item.name == item_name), None)
        if item:
            item.price = new_price  # This will also notify observers
            print(f"The price of {item_name} has been updated to {new_price}.\n")
        else:
            print(f"Item with name '{item_name}' not found in {self.name}.")

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
