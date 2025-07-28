class LinkedList:
    class Node:
        def __init__(self, data, next= None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next
        
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def insert(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.size += 1

    def add_head(self, data):
        p = self.Node(data)
        p.next = self.head
        self.head = p
        self.size += 1

    def removeHead(self):
        if self.head == None: return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def removeTail(self):
        if self.head == None : return
        if self.head.next == None:
            self.head = None
            self.size -= 1
            return
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            p.next = p.next.next
            self.size -= 1

    def insertAfter(self, i, data):
        p = self.Node(data)
        q = self.head
        count = 0
        while q != None:
            if count == i:
                p.next = q.next
                q.next = p
                return
            q = q.next
            count += 1

    def deleteAfter(self, i):
        q = self.head
        count = 0
        while q != None and q.next != None:
            if count == i:
                p = q.next
                q.next = p.next
                p = None
                self.size -= 1
                return
            q = q.next
            count += 1

    def bubble_sort(self):
        for i in range(self.size):
            p = self.head
            temp = None
            while p and p.next:
                if p.data > p.next.data:
                    next_node = p.next
                    p.data, next_node.data = next_node.data, p.data
                    print()
                    print(f"Swapping {p.next.data} and {p.data}")
                    print(f"List: {self}")

                temp = p
                p = p.next

    def printList(self):
        p = self.head
        while p != None:
            print(p.data, end="")
            p = p.next
            if p != None:
                print("->", end="")

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.data))
            node = node.next
        return '->'.join(ans)

print("*****Bubble Sort Linked List*****")
data = list(map(int, input("Enter Input: ").split(",")))
L =LinkedList()

for item in data:
    L.insert(item)

print("Input List: ",end="")
L.printList()

print()
print("_______________________________________")

L.bubble_sort()

print("_______________________________________")
print(f"Sorted List: {L}")

