class Treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data, node=None):
        node = self.root if node is None else node
        new_node = Treenode(data)
        if self.root is None:
            self.root = new_node
            return
            
        if data < node.data:
            if node.left is None:
                node.left = new_node
            else:
                self.insert(data, node.left)

        else:
            if node.right is None:
                node.right = new_node
            else:
                self.insert(data, node.right)

        return
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

bst = BST()
data = input().split(" ")
for item in data:
    bst.insert(int(item))

bst.printTree(bst.root)