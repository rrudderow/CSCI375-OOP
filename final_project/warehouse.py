#! usr/bin/env python3

"""
Warehouse Class:
* __init__
* add_item
* send_item
* remove_item
* __print__
"""

from final_project.item import Item


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

    def send_item(self, item_name: str, other: Warehouse) -> None:
        """ Sends an item from current Warehouse to other """
        item: Item = self.items.find(item_name)
        if item == -1:
            raise NameError("There is not an item by that name in the Warehouse")
        other.add_item(self.items.find(item_name))
        self.remove_item(self.item_name)

    def remove_item(self, item_name: str) -> None:
        """ Removes an item from the current Warehouse """
        self.items.remove(item_name)


    def __print__(self):
        # Prints all items in the warehouse
        if not self.items:
            print(f"{self.name} is empty.")
        else:
            print(f"Items in {self.name}:")
            for item in self.items:
                print(f"- {item.name} (ID: {item.item_id})")
