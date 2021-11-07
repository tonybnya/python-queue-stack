"""
A Queue is a linear Data Structure using the principle of `FIFO`
to insert and delete data.
`FIFO` stands for First In First Out.
Time Complexity: O(1)
"""


# Modeling a Queue using a list.
class Queue:
    """Initialize the Queue."""
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self) -> bool:
        """Method to check if the queue is empty."""

        return len(self.queue) == 0

    def is_full(self) -> bool:
        """Method to check if the queue is full."""

        return len(self.queue) == self.max_size

    # push() or enqueue()
    def push(self, data) -> None:
        """Method to add data to the queue, from the back."""

        # First check if the queue is not full
        if not self.is_full():
            self.queue.insert(0, data)

    # pop() or dequeue()
    def pop(self):
        """Method to remove and return the first item of the queue."""

        # First check if the queue is not empty
        if not self.is_empty():
            item = self.queue.pop()

        return item

    # peek() or front()
    def peek(self):
        """Method to get the item at the front of the queue."""

        # First check if the queue is not empty
        if not self.is_empty():
            item = self.queue[-1]

        return item

    def __repr__(self) -> str:
        """Method to return a string representation of the queue."""

        return repr(self.queue)
