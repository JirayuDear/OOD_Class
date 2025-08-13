class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, node=None):
        if self.root is None:
            self.root = TreeNode(data)
            return
        node = self.root if node is None else node
        new_node = TreeNode(data)
        if not self.check_insert(data):
            return
        if data < node.data:
            if node.left is None:
                node.left = new_node
                return
            self.insert(data, node.left)
        if data >= node.data:
            if node.right is None:
                node.right = new_node
                return
            self.insert(data, node.right)

    def check_insert(self, data, node=None):
        node = self.root if node is None else node
        if data == node.data:
            return False
        if node.left:
            if not self.check_insert(data ,node.left):
                return False
        if node.right:
            if not self.check_insert(data, node.right):
                return False
        return True

    def sum_all(self, sum=0, node=None):
        if not self.root:
            return
        node = self.root if node is None else node
        sum += node.data
        if node.right is None and node.left is None:
            return sum
        if node.left:
            sum = self.sum_all(sum, node.left)
        if node.right:
            sum = self.sum_all(sum, node.right)
        return sum
    
    def time_value(self, k, node=None):
        node = self.root if node is None else node
        if node.data > k:
            node.data = node.data*k
        if node.right is None and node.left is None:
            return
        if node.right:
            self.time_value(k, node.right)
        if node.left:
            self.time_value(k, node.left)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

bst = BST()
print("**Sum of tree**")
inp = input("Enter input : ").split("/")
k = int(inp[1])
data = [int(i) for i in inp[0].split(" ")]
print()

for item in data:
    bst.insert(item)

print("Tree before:")
bst.printTree(bst.root)

sum = bst.sum_all()
print(sum)

bst.time_value(k)
print("Tree after:")
bst.printTree(bst.root)
sum = bst.sum_all()
print(sum)
