class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.data)


class AVLTree:
    def __init__(self):
        self.root = None
        self.count = 0

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
                node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        if balance > 1:
            if self.balanceValue(node.left) < 0:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        return node
    
    def rightRotate(self, node):
        y = node.left
        node.left = y.right
        y.right = node
        self.updateHeight(node)
        self.updateHeight(y)
        return y
    
    def leftRotate(self, node):
        y = node.right
        node.right = y.left
        y.left = node
        self.updateHeight(node)
        self.updateHeight(y)
        return y

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

    def find_by_inOrder(self, k, node=None):
        if node:
            self.find_by_inOrder(k, node.left)
            self.count += 1
            if self.count == k:
                print(node.data)
                return 
            self.find_by_inOrder(k, node.right)
        
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


print("*** Simple but more ***")
inp = input("input  N node, Data, K small : ").split(",")
data = [int(i) for i in inp[1].split(" ")]
k = int(inp[2])

avlt = AVLTree()

for item in data:
    avlt.add(item) 

avlt.printTree(avlt.root)
avlt.find_by_inOrder(k, avlt.root)
