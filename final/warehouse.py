from item import Item
from items import Items

class Warehouse:
    def __init__(self, warehouse_id: str, location: str):
        self.warehouse_id = warehouse_id
        self.location = location
        self.inventory = Items()

    def add_item(self, item: Item):
        self.inventory.add_item(item)

    def remove_item(self, item_id: str):
        self.inventory.remove_item(item_id)

    def display_inventory(self):
        print(f"Inventory for Warehouse {self.warehouse_id} at {self.location}:")
        self.inventory.list_items()
