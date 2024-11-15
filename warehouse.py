from item import Item


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.items = []  # List to hold items in the warehouse

    def add_item(self, item):
        # Adds an item to the warehouse's list of items
        if isinstance(item, Item):
            self.items.append(item)
        else:
            print("Only Item objects can be added to the warehouse.")

    def list_items(self):
        # Prints all items in the warehouse
        if not self.items:
            print(f"{self.name} is empty.")
        else:
            print(f"Items in {self.name}:")
            for item in self.items:
                print(f"- {item.name} (ID: {item.item_id})")
