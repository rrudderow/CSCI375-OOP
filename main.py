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

# Example usage
if __name__ == "__main__":
    # Create a warehouse
    warehouse1 = Warehouse("Warehouse A")
    
    # Create some items and associate them with the warehouse
    item1 = Item("Laptop", 101, warehouse1)
    item2 = Item("Phone", 102, warehouse1)
    
    # List all items in the warehouse
    warehouse1.list_items()
    
    # Create another warehouse and an item associated with it
    warehouse2 = Warehouse("Warehouse B")
    item3 = Item("Tablet", 103, warehouse2)
    
    # List items in the second warehouse
    warehouse2.list_items()
