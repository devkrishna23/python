class Tree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def postorder_traverse(self):
        if self.left != None:
            self.left.postorder_traverse()
        if self.right != None:
            self.right.postorder_traverse()
        print(self.value, end=' ')
    
    def inorder_traverse(self):
        if self.left != None:
            self.left.inorder_traverse()
        print(self.value, end=' ')
        if self.right != None:
            self.right.inorder_traverse()
    
    def preorder_traverse(self):
        print(self.value, end=' ')
        if self.left != None:
            self.left.preorder_traverse()
        if self.right != None:
            self.right.preorder_traverse()
    
    def insertion(self, insert):
        if insert < self.value:
            if self.left == None:
                self.left = Tree(insert)
            else:
                self.left.insertion(insert)
        else:
            if self.right == None:
                self.right = Tree(insert)
            else:
                self.right.insertion(insert)

    def search(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left != None:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right != None:
                return  self.right.search(value)
            else:
                return False

    
root = Tree(2)
root.left = Tree(1)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right  = Tree(7)

