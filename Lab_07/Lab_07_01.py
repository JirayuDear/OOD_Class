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

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

inp = [int(i) for i in input('Enter Input : ').split()]
T = BST(inp[0])

inp.pop(0)
for i in inp:
    root = T.insert(i)
T.printTree(root)
# print(inp)
