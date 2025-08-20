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

    def check_sum_path(self, target, node = None, sum = 0):
        p = self.root if node is None else node
        
        sum += p.data
        
        if p.left is None and p.right is None:
            return sum == target 

        if p.left is not None:
            if self.check_sum_path(target, p.left, sum):
                return True
        if p.right is not None:
            if self.check_sum_path(target, p.right, sum):
                return True
        
        return False

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def traversal(self, node):
        if node != None:
            self.traversal(node.left)
            print(node, end=" ")
            self.traversal(node.right)

inp = [i.strip() for i in input('Enter the values to insert into BST and target sum : ').split("/")]
target = int(inp.pop())             
values = [int(i) for i in inp[0].split()]
T = BST(values[0])
values.pop(0)

for i in values:
    root = T.insert(i)

print("Inorder Traversal of BST : ", end="")
T.traversal(root) 
print()

print(f"Path with sum {target} exists : {T.check_sum_path(target)}")