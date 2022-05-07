"""
File: arraybag.py
"""

from arrays import Array

class ArrayBag:
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, source_collection=None):
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

