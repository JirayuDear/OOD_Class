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
        self.depth = 0
        self.tree_list = []

    def insert_level_order(self, data):
        new_node = Node(data)
        if not self.root:              
            self.root = new_node
            return

        q = [self.root]               
        while q:
            p = q.pop(0)               

            if not p.left:
                p.left = new_node
                return 
            else:
                q.append(p.left)

            if not p.right:
                p.right = new_node
                return 
            else:
                q.append(p.right)
            

    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self, root):
        if root is not None:
            self._inOrder(root.left)
            self._inOrder(root.right)

    # def mirror(self, depth):
    #     q = [self.root]    
    #     tree = []          
    #     while q:
    #         if q:
    #             p = q.pop(0)  
    #             tree.append(p)
    #         if p.left and p.right:
    #             q.append(p.left)
    #             q.append(p.right)

    #     if tree.pop(0) == self.root and depth == 1:
    #         p = self.root
    #         self.swap_leaf(p.left)
    #         self.swap_leaf(p.right)
    #         return

    #     for i in range(depth-1):
    #         l = tree.pop(0)
    #         r = tree.pop(0)
    def mirror(self, depth, node, current_depth=1):
        if depth == 0:
            self.swap_leaf(self.root)
            return
        if not node:
            return
        if current_depth == depth:
            self.swap_leaf(node)
            return
        if node.left:
            self.mirror(depth, node.left, current_depth + 1)
        if node.right:
            self.mirror(depth, node.right, current_depth + 1)


    def swap_leaf(self, node):
        if not node:
            return
        if node.right == None and node.left == None:
            return
        temp = node.right
        node.right = node.left
        node.left = temp

        self.swap_leaf(node.left)
        self.swap_leaf(node.right)

    def tree_make_list(self):
        q = [self.root]        
        tree_list = []
        while q:
            p = q.pop(0)  
            tree_list.append(p.data)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        return tree_list


def printTreeVisual(root, indent="", last='updown'):
    if root != None:
        print(indent, end='')
        if last == 'updown': 
            print("Root----", end='')
            indent += "       "
        elif last == 'right': 
            print("R----", end='')
            indent += "       "
        elif last == 'left': 
            print("L----", end='')
            indent += "       "
        print(root.data)
        printTreeVisual(root.left, indent, 'left') 
        printTreeVisual(root.right, indent, 'right')

print(" *** Mirror Tree ***")
inp = input("Enter nodes in level-order,depth : ").split(",")
data = [int(item) for item in inp[0].split(" ")]
depth = int(inp[1])

T = BST()
for item in data:
    T.insert_level_order(item)

print(f"before mirror: {T.tree_make_list()}")
printTreeVisual(T.root)

T.mirror(depth, T.root)

print(f"after mirror : {T.tree_make_list()}")
printTreeVisual(T.root)