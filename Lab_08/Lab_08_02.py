class AVLNode:
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

    def print_tree(self, node, level = 0):
        if node:
            self.print_tree(node.right, level + 1)
            print(f"{'    ' * level}{node}")
            self.print_tree(node.left, level + 1)


def compare_tree(tree_1, tree_2):
    if not tree_1 and not tree_2:
        return True
    if not tree_1 or not tree_2:
        return False
    if tree_1.data != tree_2.data:
        return False
    return compare_tree(tree_1.left, tree_2.left) and compare_tree(tree_1.right, tree_2.right)

avlt_1 = AVLTree()
avlt_2 = AVLTree()
inp = input("Enter Tree1/Tree2 : ").split("/")
print("Tree 1")
for item in inp[0].split():
    avlt_1.add(int(item))

avlt_1.print_tree(avlt_1.root)
print()
print("Tree 2")

for item in inp[1].split():
    avlt_2.add(int(item))

avlt_2.print_tree(avlt_2.root)
print(f"\nSame Tree" if compare_tree(avlt_1.root, avlt_2.root) else "\nDifferent Tree")