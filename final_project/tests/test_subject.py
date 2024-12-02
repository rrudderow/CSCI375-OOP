"""The module is used to test the subject.py module"""

import unittest
from unittest.mock import MagicMock
from subject import Subject
from observer import Observer


class TestSubject(unittest.TestCase):
    """Class tests Subject Class"""
    def setUp(self) -> None:
        """Set up the subject and mock observers for each test."""
        self.subject = Subject()
        self.mock_observer = MagicMock(spec=Observer)
        self.subject.register_observer(self.mock_observer)

    def test_register_observer(self) -> None:
        """Test that an observer can be registered."""
        # Verify that there is one observer after registration
        self.assertEqual(len(self.subject._observers), 1)
        self.assertIn(self.mock_observer, self.subject._observers)

    def test_remove_observer(self) -> None:
        """Test that an observer can be removed."""
        # Remove the observer
        self.subject.remove_observer(self.mock_observer)

        # Verify the observer is removed
        self.assertEqual(len(self.subject._observers), 0)
        self.assertNotIn(self.mock_observer, self.subject._observers)

    def test_notify_observers(self) -> None:
        """Test that all observers are notified when the subject changes."""
        # Register another mock observer
        another_mock_observer = MagicMock(spec=Observer)
        self.subject.register_observer(another_mock_observer)

        # Notify observers
        self.subject.notify_observers()

        # Verify that the update method was called for both observers
        self.mock_observer.update.assert_called_once()
        another_mock_observer.update.assert_called_once()

    def test_notify_no_observers(self) -> None:
        """Test that no error occurs when there are no observers."""
        subject_no_observers = Subject()
        subject_no_observers.notify_observers()
