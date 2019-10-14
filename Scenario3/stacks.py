class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        # Function to check if stack is empty
        if len(self.items) > 0:
            return False
        return True

    def clear(self):
        # Empties all elements from stack
        self.items = []

    def peek(self):
        # returns item from top of stack, but does not remove it
        if len(self.items) > 0:
            return self.items[len(self.items) - 1]
        return None

    def push(self, item):
        # Push to top of stack
        self.items.append(item)

    def pop(self):
        # Pop from top of stack
        if len(self.items) > 0:
            removedItem = self.items.pop(len(self.items) - 1)
            return removedItem
        return None