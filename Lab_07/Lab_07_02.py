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
        self.sum_path = False

    def insert(self, data, node = None):
        p = self.root if node is None else node
        if not self.root:
            self.root = Node(data)
            return
        # if self.check_insert(data):
        #     return
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
    
    # def check_insert(self, data, node = None):
    #     p = self.root if node is None else node
    #     if p.data == data:
    #         return True
    #     if p.left is not None:
    #         if self.check_insert(data, p.left):
    #             return True
    #     if p.right is not None:
    #         if self.check_insert(data, p.right):
    #             return True
    #     return False
        
    def check_sum_path(self, target, node=None):
        if node is None:
            return False
        if node.left is None and node.right is None:
            return target == node.data
        return (self.check_sum_path(target - node.data, node.left) or
                self.check_sum_path(target - node.data, node.right))
                
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def inOrder(self):
        BST._inOrder(self.root)
        
    def _inOrder(root):
        if root:
            BST._inOrder(root.left)
            print(root.data, end = ' ')
            BST._inOrder(root.right)

inp = [i.strip() for i in input('Enter the values to insert into BST and target sum : ').split(" / ")]
target = int(inp.pop())             
values = [int(i) for i in inp[0].split()]
T = BST()
for i in values:
    root = T.insert(i)
print("Inorder Traversal of BST : ", end="")
T.inOrder()
print()
print(f"Path with sum {target} exists : {T.check_sum_path(target, T.root)}")