"""This is the CLI"""

import sys
from typing import Optional
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
            table.add_row("0", "To exit")

            self.console.print(table)

            name = sys.stdin.readline()[:-1]

            if (name == "1"):
                print("what do you want to name your warehouse")
                wh_name = sys.stdin.readline()[:-1]
                warehouses.create_warehouse(wh_name)

            if (name == "2"):

                print("give the item name: ")
                item_name = sys.stdin.readline()[:-1]
                print("give the item id: ")
                item_id = sys.stdin.readline()[:-1]
                print("give the name of the warehouse to store it in: ")
                wh_name = sys.stdin.readline()[:-1]

                Item(item_name, item_id, warehouses.get_warehouse(wh_name))

            if (name == "3"):

                print("give the name of the warehouse you want to move from: ")

                move_wh = sys.stdin.readline()[:-1]

                print("what is the name of the item you want to move: ")

                itm_name = sys.stdin.readline()[:-1]

                print("what is the name of the warehouse you "
                      "want to move it to: ")

                other = sys.stdin.readline()[:-1]

                warehouses.get_warehouse(
                    move_wh).send_item(itm_name,
                                       warehouses.get_warehouse(other))

            if (name == "6"):
                table = Table(title="Warehouses")

                table.add_column("Values", justify="left",
                                 style="cyan", no_wrap=True)
                for i in warehouses.list_warehouses():

                    table.add_row(i.name)

                self.console.print(table)

            if (name == "7"):

                print("which warehouse would you like to see: ")
                name = sys.stdin.readline()[:-1]

                # print(warehouses.getWarehouse(name))

                table = Table(title=name)

                table.add_column("Item", justify="left",
                                 style="cyan", no_wrap=True)

                table.add_column("Item Count", justify="left",
                                 style="cyan", no_wrap=True)

                item_counts: Dict[str, int] = {}

                it = iter(warehouses.get_warehouse(name).items)
                while True:
                    try:
                        item = next(it)
                    except StopIteration:
                        break
                    else:  # main path
                        # output = output + "| " + repr(item) + ". Count: {}."
                        if item.name not in item_counts:
                            item_counts[item.name] = 1
                        else:
                            item_counts[item.name] += 1

                for key, value in item_counts.items():

                    table.add_row(key, str(value))

                self.console.print(table)

            if (name == "4"):
                print("please enter the name of the warehouse"
                      " you want to remove the item from: ")

                wh = sys.stdin.readline()[:-1]

                print("please enter the name of the item you want to delete")

                itemN = sys.stdin.readline()[:-1]

                warehouses.get_warehouse(wh).remove_item(itemN)

            if (name == "5"):

                print("please enter the name of the"
                      " warehouse you want to remove: ")

                wh = sys.stdin.readline()[:-1]

                warehouses.remove_warehouse(wh)
