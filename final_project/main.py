"""This program is an Inventory Management System that is able to store """

from final_project.warehouse import Warehouse
from final_project.item import Item


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
