class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stacks:
    def __init__(self):
        self.head = Node("Head")
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def peek(self):
        return self.head.value

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty Stacks")
        removed = self.head.value
        self.head = self.head.next
        return removed
        
