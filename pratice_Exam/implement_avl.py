class AVLNode:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left
        self.height = 0

    def __str__(self):
        return str(self.data)
    
class AVLTree:
    def __init__(self):
        self.root = None

    def _add(self, node, data):
        if node is None:
            return AVLNode(data)
        if data < node.data:
            node.left = self._add(node.left, data)
        else:
            node.right = self._add(node.right, data)

        return self.rebalance(node)

    def add(self, data):
        self.root = self._add(self.root, data)

    def getHeight(self, node):
        return -1 if node is None else node.height
    
    def updateHeight(self, node):
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def balanceValue(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def rebalance(self, node):
        if node is None: return node

        self.updateHeight(node)
        balance = self.balanceValue(node)
        #left + right -
        if balance < -1:
            if self.balanceValue(node.right) > 0:
                node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        if balance > 1:
            if self.balanceValue(node.left) < 0:
                node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        return node
        
    def rotateLeft(self, node):
        y = node.right
        node.right = y.left
        y.left = node 
        self.updateHeight(node)
        self.updateHeight(y)
        return y
    
    def rotateRight(self, node):
        y = node.left
        node.left = y.right
        y.right = node
        self.updateHeight(node) 
        self.updateHeight(y) 
        return y
    
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    
data = list(map(int, (input().split(" "))))
avlt = AVLTree()
for item in data:
    avlt.add(item)
avlt.printTree(avlt.root)