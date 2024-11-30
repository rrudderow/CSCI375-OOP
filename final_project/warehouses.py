"""this keeps track of warehouses and items in them"""

from typing import Optional
from typing import Any
from warehouse import Warehouse


class Warehouses:
    """class keeps track of warehouses and itmes in them"""
    _instance: Optional["Warehouses"] = None

    def __init__(self) -> None:
        """ Constructor """
        if Warehouses._instance:
            raise NameError(
                "Cannot create multiple instances of \
                a singleton class Solution")

        self._warehouses: Warehouse = []  # should be viable with subclasses of Item
        Warehouses._instance = self

    @classmethod
    def get_instance(cls) -> Optional["Warehouses"]:
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

    def create_warehouse(self, name: str) -> None :
        """creates a warehouse"""

        warehouse = Warehouse(name)
        self._warehouses.append(warehouse)

    def get_warehouse(self, name: str) -> Any:
        """returns a warehouse"""
        for i in self._warehouses:
            if name == i.name:
                return i

    def list_warehouses(self) -> list[str]:
        """returns a list of warehouses"""
        warehouses = []
        for i in self._warehouses:
            warehouses.append(i)

        return warehouses

    def show_warehouses(self) -> None:
        """prints a warehouse"""
        for i in self._warehouses:
            print(i)

    def remove_warehouse(self, warehouse_name: str) -> None:
        """ Removes a Warehuse from the current Warehouses """
        self._warehouses.remove(next((warehouse for warehouse in
                                      self._warehouses if
                                      warehouse.name == warehouse_name), None))
