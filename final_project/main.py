"""This program is an Inventory Management System that is able to store """

from datetime import date
from warehouse import Warehouse
from item import Item, Perishables


if __name__ == "__main__":
    # Create a warehouse
    warehouse1 = Warehouse("Warehouse A")
    
    # Create some items and associate them with the warehouse
    item1 = Item("Laptop", 101, warehouse1)
    item2 = Item("Phone", 102, warehouse1)
    print(item1)
    print(item2)
    
    # List all items in the warehouse
    warehouse1.list_items()
    
    # Create another warehouse and an item associated with it
    warehouse2 = Warehouse("Warehouse B")
    item3 = Item("Tablet", 103, warehouse2)
    
    # List items in the second warehouse
    warehouse2.list_items()

    # Example creation of a perishable item
    perishable_item = Perishables("Milk", "12345", date(2024, 11, 25))

    # Check if expired
    print(perishable_item.is_expired())  # Will return True or False depending on the current date

    # String representation
    print(perishable_item)  # Output: Perishable Item Milk (ID: 12345), Expiration Date: 2024-11-25
    print('\n\n')

    # Create a warehouse
    warehouse = Warehouse("Central Warehouse")

    # Create a perishable item associated with the warehouse
    perishable_item = Perishables("Milk", "12345", date(2024, 11, 25), warehouse)

    # Use @property to access attributes
    print(perishable_item.name)  # Output: Milk
    print(perishable_item.item_id)  # Output: 12345
    print(perishable_item.expiration_date)  # Output: 2024-11-25

    # Use @<property>.setter to modify attributes
    perishable_item.name = "Fresh Milk"
    perishable_item.item_id = "54321"
    perishable_item.expiration_date = date(2024, 12, 25)

    # Check the updated values
    print(perishable_item.name)  # Output: Fresh Milk
    print(perishable_item.item_id)  # Output: 54321
    print(perishable_item.expiration_date)  # Output: 2024-12-25

    # String representation
    print(perishable_item)  # Output: Perishable Item Fresh Milk (ID: 54321), Expiration Date: 2024-12-25, Warehouse: Warehouse Central Warehouse
