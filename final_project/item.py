

class Item:
    def __init__(self, name, item_id, warehouse=None):
        self.name = name
        self.item_id = item_id
        self.warehouse = warehouse

        # Automatically associate this item with the given warehouse
        if warehouse:
            warehouse.add_item(self)

    def __str__(self):
        # Return a string representation of the item
        return f"Item {self.name} (ID: {self.item_id})"
