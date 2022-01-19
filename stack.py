"""
A Stack is a linear Data Structure using the principle
of the `LIFO` or `FILO` to insert and delete data.
`LIFO` stands for Last In First Out.
`FILO` stands for First In Last Out.
Time Complexity: O(1)
"""


# Modeling a Stack using a list.
class Stack:
    """Initialize the Stack."""
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def is_empty(self) -> bool:
        """Method to check if the stack is empty."""

        return len(self.stack) == 0

    def is_full(self) -> bool:
        """Method to check if the stack is full."""

        return len(self.stack) == self.max_size

    # push() or put()
    def push(self, data):
        """Method to push data to the stack."""

        # First check if the stack is not full
        if not self.is_full():
            self.stack.append(data)

    # pop() or get()
    def pop(self):
        """Method to remove and return the last item from the stack."""

        # First check if the stack is not empty
        if not self.is_empty():
            item = self.stack.pop(0)

        return item

    # peek() or front()
    def peek(self):
        """Method to get the item at the from of the stack."""

        # First check if the stack is not empty
        if not self.is_empty():
            item = self.stack[-1]

        return item

    def __repr__(self) -> str:
        """Method to return a string representation of the stack."""

        return repr(self.stack)
