"""This module tests the observer.py module"""

import unittest
from observer import Observer


class TestObserver(unittest.TestCase):
    """Test Observer Class"""
    def setUp(self) -> None:
        """Set up an observer instance for each test."""
        self.observer = Observer()
    
    def test_update_does_not_raise_error(self) -> None:
        """Test that calling the update method does not raise an error."""
        self.observer.update()

