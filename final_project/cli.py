from typing import Optional
from rich.console import Console
from rich.table import Table
import sys
from warehouses import Warehouses
from warehouse import Warehouse
from item import Item

class Cli:
    
    _instance: Optional["Cli"] = None

    def __init__(self) -> None:
        """ Constructor """
        if Cli._instance:
            raise NameError(
                "Cannot create multiple instances of \
                a singleton class Solution")

        self.console = Console()

    def nameWarehouses(self) -> None:
        warehouses = Warehouses()
        
        name = "default"

        while name != "q":
            
            print("enter newWh to create a warehouse\n"
                  "enter addItem to add an item to a warehouse\n"
                  "enter moveItem to move an item to a new warehose\n" 
                  "enter view to see all warehouses\n"
                  "enter viewWh to see a specific warhose and its items\n")
            
            name = sys.stdin.readline()[:-1]
            
            if (name == "newWh"):
                print("what do you want to name your warehouse")
                whName = sys.stdin.readline()[:-1]
                warehouses.createWarehouse(whName)
            
            if (name == "addItem"):
                
                print("give the item name, id then name of warehouse: ")

                itemName = sys.stdin.readline()[:-1]
                itemID = sys.stdin.readline()[:-1]
                whName = sys.stdin.readline()[:-1]
                
                Item(itemName, itemID, warehouses.getWarehouse(whName))

            if (name == "moveItem"):

                print("give the name of the warehouse you want to move from: ")

                moveWh = sys.stdin.readline()[:-1]

                print("what is the name of the item you want to move: ")

                itmName = sys.stdin.readline()[:-1]

                print("what is the name of the warehouse you want to move it to: ")

                other = sys.stdin.readline()[:-1]

                warehouses.getWarehouse(moveWh).send_item(itmName, warehouses.getWarehouse(other))
                
            if (name == "view"):

                warehouses.showWarehouses()

            if (name == "viewWh"):
            
                print("which warehouse would you like to see: ")
                name = sys.stdin.readline()[:-1]

                warehouses.getWarehouse(name)
