"""Subject Class for Observer Pattern"""

from typing import List
from observer import Observer


class Subject:
    """Subject Class"""
    def __init__(self) -> None:
        """initialize"""
        self._observers: List["Observer"] = []

    def register_observer(self, observer: "Observer") -> None:
        """Add Observer"""
        self._observers.append(observer)

    def remove_observer(self, observer: "Observer") -> None:
        """Remove Observer"""
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        """Update Observer"""
        for observer in self._observers:
            observer.update()
