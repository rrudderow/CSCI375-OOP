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

        while name != "":
            
            print("1) Create a new warehouse\n"
                  "2) Add an item to a warehouse\n"
                  "3) Move an item to a new warehose\n" 
                  "4) View all items at a warehouse\n")
            
            name = sys.stdin.readline()[:-1]
            
            if (name == "1"):
                print("what do you want to name your warehouse")
                whName = sys.stdin.readline()[:-1]
                warehouses.createWarehouse(whName)
            
            if (name == "2"):
                
                print("Item name: ")
                itemName = sys.stdin.readline()[:-1]
                print("Item ID: ")
                itemID = sys.stdin.readline()[:-1]
                print("Name of Warehouse: ")
                whName = sys.stdin.readline()[:-1]
                
                Item(itemName, itemID, warehouses.getWarehouse(whName))

            if (name == "3"):

                print("give the name of the warehouse you want to move from: ")

                moveWh = sys.stdin.readline()[:-1]

                print("what is the name of the item you want to move: ")

                itmName = sys.stdin.readline()[:-1]

                print("what is the name of the warehouse you want to move it to: ")

                other = sys.stdin.readline()[:-1]

                warehouses.getWarehouse(moveWh).send_item(itmName, warehouses.getWarehouse(other))
                
            if (name == "4"):
            
                print("which warehouse would you like to see: ")
                name = sys.stdin.readline()[:-1]

                warehouses.getWarehouse(name)

    def getWarehouse(name: str) -> None:
        
