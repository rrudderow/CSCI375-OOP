"""This program is an Inventory Management System that is able to store """

from datetime import date
from warehouse import Warehouse
from item import Item
from perishables import Perishables
from cli import Cli


if __name__ == "__main__":

    cli = Cli()
    cli.nameWarehouses()
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

    # Create a warehouse
    warehouse = Warehouse("Central Warehouse")

    # Example creation of a perishable item
    perishable_item = Perishables("Milk", "12345", date(2024, 11, 25), warehouse)
    warehouse.list_items()

    # Check if expired
    print(perishable_item.is_expired())  # Will return True or False depending on the current date

    # String representation
    print(perishable_item)  # Output: Perishable Item Milk (ID: 12345), Expiration Date: 2024-11-25
    print('\n\n')

    # Create a perishable item associated with the warehouse
    perishable_item = Perishables("Milk", "12345", date(2024, 11, 25), warehouse)

    # String representation
    print(perishable_item)  # Output: Perishable Item Fresh Milk (ID: 54321), Expiration Date: 2024-12-25, Warehouse: Warehouse Central Warehouse
