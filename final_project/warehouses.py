from typing import Optional
from warehouse import Warehouse

class Warehouses:
    
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

    def createWarehouse(self, name) -> None :
        
        warehouse = Warehouse(name)
        self._warehouses.append(warehouse)

    
    def getWarehouse(self, name):
        for i in self._warehouses:
            if name == i.name:
                return i
            
    def listWarehouses(self):
        warehouses=[]
        for i in self._warehouses:
            warehouses.append(i)

        return warehouses

            
    def showWarehouses(self):
        for i in self._warehouses:
            print(i)

    def remove_Warehouse(self, warehouse_name: str) -> None:
        """ Removes a Warehuse from the current Warehouses """
        self._warehouses.remove(next((warehouse for warehouse in self._warehouses if warehouse.name == warehouse_name), None))

    
