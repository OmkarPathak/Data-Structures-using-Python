class StackedQueue:

    def __init__(self):
        self.stack = Stack()
        self.alternateStack = Stack()

    def enqueue(self, item):
        while(not self.stack.is_empty()):
            self.alternateStack.push(self.stack.pop())

        self.alternateStack.push(item)

        while(not self.alternateStack.is_empty()):
            self.stack.push(self.alternateStack.pop())
    
    def dequeue(self):
        return self.stack.pop()

    def __repr__(self):
        return repr(self.stack)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def __repr__(self):
        return str(self.items)

if __name__ == "__main__":
    structure = StackedQueue()
    structure.enqueue(4)
    structure.enqueue(3)
    structure.enqueue(2)
    structure.enqueue(1)
    print(structure)
    structure.dequeue()
    print(structure)