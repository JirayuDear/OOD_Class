class avltNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.data)


    def setHeight(self):
        lheight = self.get_height(self.left)
        rheight = self.get_height(self.right)
        self.height = 1 + max(lheight, rheight)
        return self.height
    
    def get_height(self, node):
        if not node:
            return -1
        return node.height
    
    def balanceVal(self):
        lheight = self.get_height(self.left)
        rheight = self.get_height(self.right)
        return lheight - rheight

    def __str__(self):
        return str(self.data)
    
class avltTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def getHeight(self, node):
        return -1 if node is None else node.height

    def updateHeight(self, node):
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def balanceValue(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self.updateHeight(x)
        self.updateHeight(y)
        return y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        self.updateHeight(x)
        self.updateHeight(y)
        return y

    def rebalance(self, node):
        if node is None:
            return node

        self.updateHeight(node)
        balance = self.balanceValue(node)

        # Right heavy
        if balance < -1:
            if self.balanceValue(node.right) > 0:
                node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        # Left heavy
        if balance > 1:
            if self.balanceValue(node.left) < 0:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        return node

    def _add(self, node, data):
        if node is None:
            return avltNode(data)
        if data < node.data:
            node.left = self._add(node.left, data)
        else:
            node.right = self._add(node.right, data)

        return self.rebalance(node)

    def add(self, data):
        self.root = self._add(self.root, data)

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def max_sum(self, node, path = None):
        if not self.root:
            return 0
        if not path:
            path = []
        if node:
            path.append(node.data)
            return self.max_sum(node.right, path.copy()) if node.right else self.max_sum(node.left, path.copy())
        return path, sum(path)

avlt = avltTree()
inp = input("Enter tree nodes: ").split()
for item in inp:
    avlt.add(int(item))
avlt.printTree(avlt.root)
path, length = avlt.max_sum(avlt.root)
path_sum = ' + '.join(map(str, path))
print()
print(f"Path with maximum sum: {path_sum} = {length}")