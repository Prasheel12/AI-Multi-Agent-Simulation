class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        #Check if stack is empty
        if len(self.items) > 0:
            return False
        return True
    
    def clear(self):
        #Clears stack
        self.items = []

    def peek(self):
        #Return data at top of stack
        if len(self.items) > 0:
            return self.items[len(self.items)-1]
        return None

    def push(self, item):
        #Push new data to top of stack
        self.items.append(item)

    def pop(self):
        #Pop from top of stack
        if len(self.items) > 0:
            removedItem = self.items.pop(len(self.items)-1)
            return removedItem
        return None
