class Node:
    def __init__(self, data, next= None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.zero = 0

    def insert(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.size += 1

    def add_head(self, data):
        p = Node(data)
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
        p = Node(data)
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

    def printList(self):
        p = self.head
        while p != None:
            print(p.data, end="")
            p = p.next
            if p != None:
                print(" <- ", end="")

    def find_zero(self):
        p = self.head
        self.link_before_zero = LinkedList()
        while p != None:
            if p.data == 0: 
                self.zero = p
                return self.remove_before_zero()
            else:
                self.link_before_zero.insert(p.data)
            p = p.next
        
    def remove_before_zero(self):
        p = self.head
        while p.data != 0:
            self.removeHead()
            p = p.next
        return self.extend_top_zero()
    
    def extend_top_zero(self):
        p = self.link_before_zero.head
        while p:
            self.insert(p.data)
            p = p.next


print(" *** Locomotive ***")
data = list(map(int, input("Enter Input : ").split(" ")))
L = LinkedList()
for item in data:
    L.insert(item)
print("Before : ",end="")

L.printList()

L.find_zero()
print()
print("After : ",end="")
L.printList()