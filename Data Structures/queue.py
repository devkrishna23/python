class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self, head, tail):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        new = Node(value)
        if self.head is None and self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
    
    def dequeue(self):
        value = self.head.value 
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.value