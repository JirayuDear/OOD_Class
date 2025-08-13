class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, node=None):
        node = self.root if node is None else node

        if node is None: 
            self.root = TreeNode(data)
            return self.root

        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self.insert(data, node.left)
        else:  
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self.insert(data, node.right)
        return self.root
    
    def insert_level_order(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return
        new_node = TreeNode(data)
        q = [self.root]
        while q:
            p = q.pop(0)
            if p.left is None:
                p.left = new_node
                return self.root
            else:
                q.append(p.left)
            
            if p.right is None:
                p.right = new_node
                return self.root
            else:
                q.append(p.right)

    def get_list_tree(self, len_data):
        q = [self.root]
        tree_list = [self.root.data]
        for i in range(len_data):
            while q:
                p = q.pop(0)
                if p.left is not None:
                    q.append(p.left)
                    tree_list.append(p.left.data)
                if p.right is not None:
                    q.append(p.right)
                    tree_list.append(p.right.data)
        return tree_list
    
    def swap(self, node=None):
        if node is None:
            return
        if node.right == None and node.left == None:
            return

        temp = node.right
        node.right = node.left
        node.left = temp

        self.swap(node.right) 
        self.swap(node.left) 
    
    def mirror(self, depth, node = None):
        if depth == -1:
            self.swap(self.root)
            return
        node = self.root if node is None else node
        if depth == 0:
            self.swap(node)
            return
        self.mirror(depth-1, node.right)
        self.mirror(depth-1, node.left)
        
    
       
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



bst = BST()
print(" *** Mirror Tree ***")
inp = input("Enter nodes in level-order,depth : ").split(",")
depth_mirror = int(inp[1])
data = inp[0].split(" ")
data = [int(i) for i in data]

len_data = len(data)

for item in data:
    root = bst.insert_level_order(item)

print(f"before mirror: {bst.get_list_tree(len_data)}")
printTreeVisual(root)

bst.mirror(depth_mirror-1)
print(f"after mirror: {bst.get_list_tree(len_data)}")

printTreeVisual(root)
