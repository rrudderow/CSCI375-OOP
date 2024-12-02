"""This is the CLI"""

import sys
from typing import Optional, Dict
from rich.console import Console
from rich.table import Table
from warehouses import Warehouses
from item import Item


class Cli:
    """class that runs the CLI"""

    _instance: Optional["Cli"] = None

    def __init__(self) -> None:
        """ Constructor """
        if Cli._instance:
            raise NameError(
                "Cannot create multiple instances of \
                a singleton class Solution")

        self.console = Console()
        Cli._instance = self

    @classmethod
    def get_instance(cls) -> Optional["Cli"]:
        """Returns the instance of the class

        Returns:
            Solution: class instance
        """
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """Resets the instance
        """
        cls._instance = None

    def run_cli(self) -> None:
        """this runs the cli"""
        warehouses = Warehouses()

        name = "default"

        while name != "0":

            self.options()

            name = sys.stdin.readline()[:-1]

            if (name == "1"):
                self.op_one(warehouses)

            if (name == "2"):
                self.op_two(warehouses)

            if (name == "3"):
                self.op_three(warehouses)

            if (name == "4"):
                self.op_four(warehouses)

            if (name == "5"):
                self.op_five(warehouses)

            if (name == "6"):
                self.op_six(warehouses)

            if (name == "7"):
                self.op_seven(warehouses)

            if (name == "8"):
                self.op_eight(warehouses)

    def options(self) -> None:
        """Output Table CLI"""
        table = Table(title="Options")

        table.add_column("Values", justify="right",
                         style="cyan", no_wrap=True)
        table.add_column("Definition", justify="left",
                         style="cyan", no_wrap=True)

        table.add_row("1", "create a warehouse")
        table.add_row("2", "add an item to a warehouse")
        table.add_row("3", "move an item to a new warehose")
        table.add_row("4", "delete an item")
        table.add_row("5", "remove a warehouse")
        table.add_row("6", "view all warehouses")
        table.add_row("7", "view a specific warehouse and its items")
        table.add_row("8", "change an item's price")
        table.add_row("0", "To exit")

        self.console.print(table)

    def op_one(self, warehouses: Warehouses) -> None:
        """Create Warehouse"""
        print("what do you want to name your warehouse")
        wh_name = sys.stdin.readline()[:-1]
        warehouses.create_warehouse(wh_name)

    def op_two(self, warehouses: Warehouses) -> None:
        """Add Item"""
        print("give the item name: ")
        item_name = sys.stdin.readline()[:-1]
        print("give the item id: ")
        item_id = sys.stdin.readline()[:-1]
        print("give the name of the warehouse to store it in: ")
        wh_name = sys.stdin.readline()[:-1]
        print("give the item's price: ")
        it_price = sys.stdin.readline()[:-1]

        Item(item_name, int(item_id), float(it_price),
             warehouses.get_warehouse(wh_name))
        # warehouses.get_warehouse(wh_name).add_item(Item)

    def op_three(self,  warehouses: Warehouses) -> None:
        """Move Item"""
        print("give the name of the warehouse you want to move from: ")

        move_wh = sys.stdin.readline()[:-1]

        print("what is the name of the item you want to move: ")

        itm_name = sys.stdin.readline()[:-1]

        print("what is the name of the warehouse you "
              "want to move it to: ")

        other = sys.stdin.readline()[:-1]

        move_ware = warehouses.get_warehouse(move_wh)
        if not move_ware:
            raise ValueError(f"Warehouse {move_wh} does not exist.")

        other_ware = warehouses.get_warehouse(other)
        if not other_ware:
            raise ValueError(f"Warehouse {other} does not exist.")

        move_ware.send_item(itm_name, other_ware)

    def op_four(self, warehouses: Warehouses) -> None:
        """Remove Item"""
        print("please enter the name of the warehouse"
              " you want to remove the item from: ")

        wh = sys.stdin.readline()[:-1]

        print("please enter the name of the item you want to delete")

        itemN = sys.stdin.readline()[:-1]

        ware = warehouses.get_warehouse(wh)
        if not ware:
            raise ValueError(f"Warehouse {wh} does not exist.")
        ware.remove_item(itemN)

    def op_five(self, warehouses: Warehouses) -> None:
        """Remove Warehouse"""
        print("please enter the name of the"
              " warehouse you want to remove: ")

        wh = sys.stdin.readline()[:-1]

        warehouses.remove_warehouse(wh)

    def op_six(self, warehouses: Warehouses) -> None:
        """Print Warehouses"""
        table = Table(title="Warehouses")

        table.add_column("Values", justify="left",
                         style="cyan", no_wrap=True)
        for i in warehouses.list_warehouses():

            table.add_row(i.name)

        self.console.print(table)

    def op_seven(self, warehouses: Warehouses) -> None:
        """Print Items at Warehouse"""
        print("which warehouse would you like to see: ")
        name = sys.stdin.readline()[:-1]

        # print(warehouses.getWarehouse(name))

        table = Table(title=name)

        table.add_column("Item", justify="left",
                         style="cyan", no_wrap=True)

        table.add_column("Item Count", justify="left",
                         style="cyan", no_wrap=True)

        ware = warehouses.get_warehouse(name)
        if not ware:
            raise ValueError(f"Warehouse {name} does not exist..")
        item_counts: Dict[str, int] = ware.cli_items()

        for key, value in item_counts.items():

            table.add_row(key, str(value))

        self.console.print(table)

    def op_eight(self, warehouses: Warehouses) -> None:
        """Change Item Price"""
        print("What is the item you would like to change: ")
        item_name = sys.stdin.readline()[:-1]
        print("What should the new price be: ")
        new_price = sys.stdin.readline()[:-1]

        found_item = False
        # Iterate through all warehouses
        for warehouse in warehouses.list_warehouses():
            # Look for the item in this warehouse
            item = next((item for item in warehouse.items if
                         item.name == item_name), None)

            if item:
                # If the item is found, update its price
                # Directly update the item's price
                item.price = float(new_price)
                print(f"The price of '{item_name}' has"
                      f" been updated to {new_price}.")
                found_item = True
                break  # Exit the loop after updating the item

        if not found_item:
            print(f"Item '{item_name}' not found in any warehouse.")
