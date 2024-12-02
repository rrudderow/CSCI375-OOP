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
from observer import Observer


class Warehouse(Observer):
    def __init__(self, name: str) -> None:
        """ Constructor """
        self._name: str = name
        self._items: List[Item] = []

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
        item = self.find_item(item_name)
        if not item:
            raise ValueError(f"Item '{item_name}' not found in {self.name}.")
        other.add_item(item)
        self.remove_item(item_name)

    def find_item(self, itm_name: str) -> Item | None:
        """ Finds an item given its name """
        for itm in self.items:
            if itm.name == itm_name:
                return itm
        return None

    def remove_item(self, itm_name: str) -> None:
        """ Removes an item from the current Warehouse """
        item = self.find_item(itm_name)
        if not item:
            raise ValueError(f"Item '{itm_name}' not found.")
        item.remove_observer(self)
        self.items.remove(item)

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

    def update(self) -> None:
        """update price"""
        print(f"{self.name} has been notified about the price change.")

    def update_item_price(self, item_name: str, new_price: float) -> None:
        """Finds an item by its name and updates its price."""
        item = next((item for item in self.items
                     if item.name == item_name), None)
        if item:
            item.price = new_price  # This will also notify observers
            print(f"The price of {item_name} \
                  has been updated to {new_price}.\n")
        else:
            print(f"Item with name '{item_name}' not found in {self.name}.")
