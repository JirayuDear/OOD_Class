class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self, root = None):
        self.root = None if root is None else Node(root)

    def insert(self, data, node = None):
        p = self.root if node is None else node
        if not self.root:
            self.root = Node(data)
            return
        if self.check_insert(data):
            return
        if self.root != None:
            if data >= p.data and p.right == None:
                p.right = Node(data)
                return
            elif data < p.data and p.left == None: 
                p.left = Node(data)
                return
            elif data >= p.data:
                self.insert(data, p.right)
            elif data < p.data:
                self.insert(data, p.left)
        return self.root
    
    def check_insert(self, data, node = None):
        p = self.root if node is None else node
        if p.data == data:
            return True
        if p.left is not None:
            if self.check_insert(data, p.left):
                return True
        if p.right is not None:
            if self.check_insert(data, p.right):
                return True
        return False
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def sum_path(self, node=None, sum = 0):
        p = self.root if node is None else node
        sum += p.data
        if p.left is None and p.right is None:
            return sum
        if p.right is not None:
            sum = self.sum_path(p.right, sum)
        if p.left is not None:
            sum = self.sum_path(p.left, sum) 
        return sum
    
    def change_value(self, k, node=None):
        p = self.root if node is None else node
        if p.data > k:
            p.data = p.data*k
        if p.left is None and p.right is None:
            return
        if p.right is not None:
            self.change_value(k, p.right)
        if p.left is not None:
            self.change_value(k, p.left) 
        
        
    
print("**Sum of tree**")
data = input("Enter input : ").split("/")
k = data[1]
data = data[0].split(" ")
data = [int(i) for i in data]

B = BST()

for item in data:
    B.insert(item)

print()
print("Tree before:")
B.printTree(B.root)
print(f"Sum of all nodes = {B.sum_path()}")
print()
print("Tree after: ")
B.change_value(int(k))
B.printTree(B.root)
print(f"Sum of all nodes = {B.sum_path()}")