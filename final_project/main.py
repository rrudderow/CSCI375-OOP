"""This program is an Inventory Management System that is able to store """

from datetime import date
from warehouse import Warehouse
from item import Item
from cli import Cli


if __name__ == "__main__":

    cli = Cli()
    cli.run_cli()
