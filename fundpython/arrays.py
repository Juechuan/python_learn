class Array:
    """Represents an array"""

    def __init__(self, capacity, fill_value=None):
        """Capacity is the static size of the array.
        fill_value is placed at each position.
        """
        self.items = []
        for count in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        """The capacity of the array."""
        return len(self.items)

    def __str__(self) -> str:
        """The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """supports traversal with a for loop."""

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, new_item):
        """Subscript operator for replacement at index."""
        self.items[index] = new_item
