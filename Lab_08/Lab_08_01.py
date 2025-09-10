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
            return AVLNode(data)
        if data < node.data:
            node.left = self._add(node.left, data)
        else:
            node.right = self._add(node.right, data)

        return self.rebalance(node)

    def add(self, data):
        self.root = self._add(self.root, data)

    def inorder(self, node, position):
        if node:
            self.inorder(node.left, position)
            self.count += 1
            if self.count == position:
                print(node.data)
                return
            self.inorder(node.right, position)
        
        
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


print("*** Simple but more ***")
data = input("input  N node, Data, K small : ").split(",")
node = int(data[0])
k = int(data[2])
data = [int(item) for item in data[1].split(" ")]

avlT = AVLTree()
for i in range(node):
    avlT.add(data[i])

avlT.inorder(avlT.root, int(k))