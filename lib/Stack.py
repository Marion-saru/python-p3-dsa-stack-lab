# lib/Stack.py

class Stack:
    """
    A simple Stack implementation using a Python list.
    The top of the stack is considered the end of the list.
    """

    def __init__(self, initial_list=None, max_size=None):
        """
        Initializes the Stack.

        Args:
            initial_list (list, optional): A list to initialize the stack with.
                                            Defaults to an empty list.
            max_size (int, optional): The maximum capacity of the stack.
                                      If None, the stack has no size limit.
        """
        # The internal list to store stack elements
        self.items = []
        if initial_list is not None:
            # Extend the items list with the initial list elements
            # This ensures that if initial_list is [1,2,3], items becomes [1,2,3]
            self.items.extend(initial_list)
        self.max_size = max_size

    def push(self, item):
        """
        Adds an item to the top of the stack.

        Args:
            item: The item to be added to the stack.
        """
        # Check if the stack is full before pushing
        if self.max_size is not None and len(self.items) >= self.max_size:
            print("Error: Stack is full. Cannot push item.")
            return
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the item from the top of the stack.

        Returns:
            The item removed from the top of the stack.
            Returns None if the stack is empty.
        """
        # Check if the stack is empty before popping
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Error: Stack is empty. Cannot pop item.")
            return None

    def size(self):
        """
        Returns the current number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)

    def isEmpty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def full(self):
        """
        Checks if the stack is full.

        Returns:
            bool: True if the stack has a maximum size and is at capacity,
                  False otherwise.
        """
        # A stack is full only if it has a defined max_size and its current
        # size equals that max_size. If max_size is None, it's never full.
        return self.max_size is not None and len(self.items) == self.max_size

    def search(self, element):
        """
        Searches for an element in the stack and returns its "distance" from the top.
        The distance is defined as the number of elements from the top of the stack,
        where the top element is at distance 0, the next is at distance 1, and so on.
        If the element is not found, returns -1.

        Args:
            element: The element to search for.

        Returns:
            int: The distance of the element from the top of the stack (0-indexed),
                 or -1 if the element is not found.
        """
        try:
            # Find the index of the element from the bottom of the list
            index_from_bottom = self.items.index(element)
            # Calculate the distance from the top
            # len(self.items) - 1 is the index of the top element
            # Subtracting index_from_bottom gives the distance from the top
            return len(self.items) - 1 - index_from_bottom
        except ValueError:
            # Element not found in the list
            return -1

