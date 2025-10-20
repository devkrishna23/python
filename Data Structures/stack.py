class Stack:
    def __init__(self, stack = None):
        if stack is None:
            self.stack = []
        else:
            self.stack = stack

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack) == 0:
            return "Empty stack"
        else:
            return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def size(self):
        return len(self.stack)
    
    def display(self):
         print(self.stack)