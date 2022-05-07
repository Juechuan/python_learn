"""
File: baginterface.py
"""


class BagInterface:
    def __init__(self, souce_collection=None):
        """Sets the initial state of self, which incudes the contents of sourceCollection, if it is presents."""
        pass

    def is_empty(self):
        """Returns the number of items in self."""
        return True

    def __len__(self):
        """Returns the number of items in self."""
        return 0 

    def __str__(self):
        """Returns the string presentation of self."""
        return ''

    def __iter__(self):
        """Supports iteration over a view of self."""
        return None

    def __add__(self, other):
        """Returns a new bag containing the contents of self and other"""
        return None

    def __eq__(self, other):
        """Return True if self equals other, or False otherwise."""
        return False

    def count(self, item):
        """Return the number of instances of item in self."""
        return 0

    # Mutator methods
    def clear(self):
        """Make self become empty."""
        pass

    def add(self, item):
        """Add item to self."""
        pass

    def remove(self, item):
        """
        Precondition: item is in self.
        Raises: KeyError if item in nor in self.
        Postcondition: item is removed from self.
        """
        pass
