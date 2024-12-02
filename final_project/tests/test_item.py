"""This module is used to test the item.py module"""

import unittest
from unittest.mock import MagicMock, patch
from hypothesis import given, strategies as st
from item import Item


class TestItem(unittest.TestCase):
    """Tests Item Class"""
    def setUp(self) -> None:
        """Setup the basic mocks and objects for each test."""
        # Create a mock warehouse
        self.mock_warehouse = MagicMock()
        # Create an Item instance
        self.item = Item(name="Test Item", item_id=123,
                         price=10.99, warehouse=self.mock_warehouse)

    def test_initialization(self) -> None:
        """Test that the Item is initialized correctly."""
        # Check if the attributes are set correctly
        self.assertEqual(self.item.name, "Test Item")
        self.assertEqual(self.item.item_id, 123)
        self.assertEqual(self.item.price, 10.99)
        self.assertEqual(self.item.warehouse, self.mock_warehouse)

    @patch.object(Item, 'notify_observers', MagicMock())
    def test_price_update_notify(self) -> None:
        """Test price change triggers observer notification"""
        with patch.object(self.item, 'notify_observers',
                          MagicMock()) as mock_notify:
            # Change the price
            self.item.price = 15.99

            mock_notify.assert_called_once()

    def test_no_notify_on_same_price(self) -> None:
        """Test that no notification occurs when the price is the same."""
        # Using patch again to mock the method inside the test
        with patch.object(self.item, 'notify_observers',
                          MagicMock()) as mock_notify:
            # Change the price to the same value
            self.item.price = 10.99

            # Assert that no observer notification was called
            mock_notify.assert_not_called()

    @given(st.text(), st.integers(), st.floats(min_value=0.0))
    def test_item_properties(self, name: str, item_id: int,
                             price: float) -> None:
        """Test the Item constructor with various inputs using Hypothesis."""
        item = Item(name=name, item_id=item_id, price=price, warehouse=None)

        # Validate that the item properties are set correctly
        self.assertEqual(item.name, name)
        self.assertEqual(item.item_id, item_id)
        self.assertEqual(item.price, price)

    def test_repr(self) -> None:
        """Test the __repr__ method of Item."""
        expected_repr = "Item Test Item (ID: 123) Price: $10.99"
        self.assertEqual(repr(self.item), expected_repr)

    def test_warehouse_association_on_init(self) -> None:
        """Test that the warehouse is associated correctly when provided."""
        # Verify that the add_item method of warehouse is called
        self.mock_warehouse.add_item.assert_called_once_with(self.item)

    def test_name_setter(self) -> None:
        """Test the setter for the name property."""
        self.item.name = "New Name"
        self.assertEqual(self.item.name, "New Name")

    def test_item_id_setter(self) -> None:
        """Test the setter for the item_id property."""
        self.item.item_id = 999
        self.assertEqual(self.item.item_id, 999)

    def test_price_setter(self) -> None:
        """Test the setter for the price property."""
        self.item.price = 25.50
        self.assertEqual(self.item.price, 25.50)

    def test_warehouse_setter(self) -> None:
        """Test the setter for the warehouse property."""
        new_warehouse = MagicMock()
        self.item.warehouse = new_warehouse
        self.assertEqual(self.item.warehouse, new_warehouse)
