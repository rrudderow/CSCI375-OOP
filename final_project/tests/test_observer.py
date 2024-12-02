"""This module tests the observer.py module"""

import unittest
from observer import Observer


class TestObserver(unittest.TestCase):
    """Test Observer Class"""
    def setUp(self):
        """Set up an observer instance for each test."""
        self.observer = Observer()
    
    def test_update_returns_none(self):
        """Test that the update method returns None."""
        result = self.observer.update()
        self.assertIsNone(result, "The update method should return None.")

