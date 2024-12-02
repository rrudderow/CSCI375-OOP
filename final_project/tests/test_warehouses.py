"""tests the Warehouses class"""

import unittest
from warehouses import Warehouses


class TestWarehouses(unittest.TestCase):
    """tests the Warehouses class"""

    def test_instance(self) -> None:
        """tests get/reset_instance"""

        Warehouses.reset_instance()

        self.assertIsNone(Warehouses.get_instance())

        _ = Warehouses()

        try:
            _ = Warehouses()

        except NameError:
            pass

        self.assertIsNotNone(Warehouses.get_instance())
