"""This module is used to test the item.py module"""

import unittest
from unittest.mock import MagicMock
from hypothesis import given, strategies as st
from item import Item


class TestItem(unittest.TestCase):
    """Tests Item Class"""
    def setUp(self):
        """Setup the basic mocks and objects for each test."""
        # Create a mock warehouse
        self.mock_warehouse = MagicMock()
        # Create an Item instance
        self.item = Item(name="Test Item", item_id=123, price=10.99, warehouse=self.mock_warehouse)

    def test_initialization(self):
        """Test that the Item is initialized correctly."""
        # Check if the attributes are set correctly
        self.assertEqual(self.item.name, "Test Item")
        self.assertEqual(self.item.item_id, 123)
        self.assertEqual(self.item.price, 10.99)
        self.assertEqual(self.item.warehouse, self.mock_warehouse)

    def test_price_update_notify(self):
        """Test that the price change triggers observer notification."""
        # Mock the observer notification method
        self.item.notify_observers = MagicMock()

        # Change the price
        self.item.price = 15.99

        # Assert that the observer notification was called when the price changes
        self.item.notify_observers.assert_called_once()

    def test_no_notify_on_same_price(self):
        """Test that no notification occurs when the price is the same."""
        self.item.notify_observers = MagicMock()
        
        # Change the price to the same value
        self.item.price = 10.99
        
        # Assert that no observer notification was called
        self.item.notify_observers.assert_not_called()

    @given(st.text(), st.integers(), st.floats(min_value=0.0))
    def test_item_properties(self, name, item_id, price):
        """Test the Item constructor with various inputs using Hypothesis."""
        item = Item(name=name, item_id=item_id, price=price, warehouse=None)
        
        # Validate that the item properties are set correctly
        self.assertEqual(item.name, name)
        self.assertEqual(item.item_id, item_id)
        self.assertEqual(item.price, price)

    def test_repr(self):
        """Test the __repr__ method of Item."""
        expected_repr = f"Item Test Item (ID: 123) Price: $10.99"
        self.assertEqual(repr(self.item), expected_repr)

    def test_warehouse_association_on_init(self):
        """Test that the warehouse is associated correctly when provided."""
        # Verify that the add_item method of warehouse is called
        self.mock_warehouse.add_item.assert_called_once_with(self.item)

    def test_name_setter(self):
        """Test the setter for the name property."""
        self.item.name = "New Name"
        self.assertEqual(self.item.name, "New Name")

    def test_item_id_setter(self):
        """Test the setter for the item_id property."""
        self.item.item_id = 999
        self.assertEqual(self.item.item_id, 999)

    def test_price_setter(self):
        """Test the setter for the price property."""
        self.item.price = 25.50
        self.assertEqual(self.item.price, 25.50)

    def test_warehouse_setter(self):
        """Test the setter for the warehouse property."""
        new_warehouse = MagicMock()
        self.item.warehouse = new_warehouse
        self.assertEqual(self.item.warehouse, new_warehouse)
