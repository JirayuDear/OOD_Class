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
        self.found = False
        self.found_es = False
        self.mission = False

    def insert(self, data, node = None):
        p = self.root if node is None else node
        if not self.root:
            self.root = Node(data)
            return
        if self.check_insert(data):
            return
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
    
    def check_insert(self, data, node = None):
        p = self.root if node is None else node
        if p.data == data:
            return True
        if p.left is not None:
            if self.check_insert(data, p.left):
                return True
        if p.right is not None:
            if self.check_insert(data, p.right):
                return True
        return False
        
    def find_treasure_escape(self, treasure, escape, node=None, path=None):
        if node is None:
            node = self.root
            path = []

        if node.data == treasure:
            self.found = True
            print("Found Treasure !!!")

        if node.data == escape and self.found:
            self.found_es = True
            self.mission = True
            print("Found Escape !!!")
            path.append(node.data)
            print("✅ ", end="")
            print(" -> ".join(map(str, path)))
            return True
        
        if self.mission:
            return

        path.append(node.data)
        print("❌ ", end="")
        print(" -> ".join(map(str, path)))

        if node.left is None and node.right is None:
            path.pop()
            return
        
        if node.left is not None:
            result = self.find_treasure_escape(treasure, escape, node.left, path)
            if result:
                return print(">>> Mission Complete <<< ")

        if node.right is not None:
            result = self.find_treasure_escape(treasure, escape, node.right, path)
            if result:
                return print(">>> Mission Complete <<< ")
            
        path.pop()

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


inp = input("Enter Input : ").split("/")
data = [int(item) for item in inp[0].split(" ")]
treasure = int(inp[1])
escape = int(inp[2])

B = BST()

for item in data:
    B.insert(item)

B.printTree(B.root)
print("-------------------------------------------------")
B.find_treasure_escape(treasure, escape)
if not B.found_es:
    print(">>> Mission Failed <<<")
