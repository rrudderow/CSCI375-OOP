"""This module tests the warehouse.py module"""

from typing import Dict
import unittest
from hypothesis import given
import hypothesis.strategies as some
from unittest.mock import patch, MagicMock
from item import Item
from warehouse import Warehouse


class TestWarehouse(unittest.TestCase):
    """Test Warehouse Class"""
    def setUp(self) -> None:
        """Setup method to create a new Warehouse for each test."""
        self.warehouse = Warehouse(name="Main Warehouse")
        self.warehouse1 = Warehouse(name="Warehouse 1")
        self.warehouse2 = Warehouse(name="Warehouse 2")

    @patch('item.Item')  # Mocking the Item class
    def test_add_item(self, MockItem: MagicMock) -> None:
        """Test adding an item to the warehouse."""
        # Creating a mock Item
        mock_item = MockItem.return_value
        mock_item.name = "item1"

        # Add the mock item to the warehouse
        self.warehouse.add_item(mock_item)

        # Assert the item is in the warehouse
        self.assertEqual(len(self.warehouse.items), 1)
        self.assertEqual(self.warehouse.items[0], mock_item)
        mock_item.register_observer.assert_called_once_with(self.warehouse)

    @patch('item.Item')
    def test_remove_item(self, MockItem: MagicMock) -> None:
        """Test removing an item from the warehouse."""
        mock_item = MockItem.return_value
        mock_item.name = "item1"
        self.warehouse.add_item(mock_item)

        # Remove the item
        self.warehouse.remove_item("item1")

        # Check if the item was removed from the warehouse
        self.assertEqual(len(self.warehouse.items), 0)
        mock_item.remove_observer.assert_called_once_with(self.warehouse)

    @patch('item.Item')
    def test_find_item(self, MockItem: MagicMock) -> None:
        """Test finding an item in the warehouse."""
        mock_item = MockItem.return_value
        mock_item.name = "item1"
        self.warehouse.add_item(mock_item)

        found_item = self.warehouse.find_item("item1")
        self.assertEqual(found_item, mock_item)

        # Test when the item is not found
        not_found_item = self.warehouse.find_item("item2")
        self.assertIsNone(not_found_item)

    @patch("warehouse.Warehouse.find_item")
    @patch("warehouse.Warehouse.remove_item")
    @patch("warehouse.Warehouse.add_item")
    def test_send_item_success(self, mock_add_item: MagicMock,
                               mock_remove_item: MagicMock,
                               mock_find_item: MagicMock) -> None:
        """Test sending an item from one warehouse to another."""

        # Create a mock item and mock its behavior
        mock_item = MagicMock(spec=Item)
        mock_item.name = "item1"

        # Mock the `find_item` method to return the mock item
        mock_find_item.return_value = mock_item

        # Call send_item to transfer the item
        self.warehouse1.send_item("item1", self.warehouse2)

        # Assert that the item was added to the other warehouse
        mock_add_item.assert_called_once_with(mock_item)

        # Assert that the item was removed from the original warehouse
        mock_remove_item.assert_called_once_with("item1")

        # Ensure the item was found by the `find_item` method
        mock_find_item.assert_called_once_with("item1")

    @patch("warehouse.Warehouse.find_item")
    def test_send_item_item_not_found(self, mock_find_item: MagicMock) -> None:
        """Test sending an item when the item is not found in the warehouse."""

        # Mock `find_item` to return None (item not found)
        mock_find_item.return_value = None

        # Assert ValueError when the item is not found
        with self.assertRaises(ValueError):
            self.warehouse1.send_item("non_existent_item",
                                      self.warehouse2)

    @given(
        wh_name=some.text(min_size=1, max_size=50),
        items=some.lists(
            some.tuples(
                some.text(min_size=1, max_size=50),
                some.integers(min_value=1, max_value=100),
                some.floats(min_value=0.01, max_value=1000),
            ),
            min_size=1,
            max_size=20
        )
    )
    def test_cli_items(self, wh_name: str,
                       items: list[tuple[str, int, float]]) -> None:
        """Test cli_items method with random data."""
        warehouse = Warehouse(wh_name)
        for item_name, item_id, item_price in items:
            warehouse.add_item(Item(item_name, item_id, item_price, warehouse))

        cli_counts: Dict[str, int] = warehouse.cli_items()
        expected_counts: Dict[str, int] = {}
        for item in warehouse.items:
            if repr(item) not in expected_counts:
                expected_counts[repr(item)] = 1
            else:
                expected_counts[repr(item)] += 1

        self.assertEqual(cli_counts, expected_counts)

    @patch("builtins.print")
    def test_update(self, mock_print: MagicMock) -> None:
        """Test update method to check if the correct message is printed."""
        # Call the update method
        self.warehouse.update()
        # Assert that print was called with the expected message
        mock_print.assert_called_once_with(
            "Main Warehouse has been notified about the "
            "price change."
        )

    @patch('item.Item')
    def test_update_item_price(self, MockItem: MagicMock) -> None:
        """Test updating the price of an item."""
        mock_item = MockItem.return_value
        mock_item.name = "item1"
        mock_item.price = 10.0
        self.warehouse.add_item(mock_item)

        # Update price
        self.warehouse.update_item_price("item1", 15.0)

        # Assert the price was updated
        self.assertEqual(mock_item.price, 15.0)
