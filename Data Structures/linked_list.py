class Node:
    def __init__(self, value ,next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def insertion(self, value):
        node = Node(value, self.head)
        self.head = node
    
    def traverse(self):
        current = self.head
        while self.head is not None:
            print(current.value)
            current = current.next
    
    def push(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while True:
                if current.next is None:
                    current.next = new
                    break
                current = current.next
    

            
