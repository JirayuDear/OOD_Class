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
        self.prev_repo = 0
        self.same_repo = False
        self.queen_limit = 0
        self.size = 0
        self.zero = 0
        self.index = 0

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
                print(" → ", end="")

    def new_order(self, k):
        if k <= 1 or self.head is None:
            return

        curr = self.head
        prev_end = None  
        is_reverse = True

        while curr:
            group_start = curr
            group_end = curr

            for i in range(k - 1):
                if group_end.next:
                    group_end = group_end.next
                else:
                    return

            next_group = group_end.next

            if is_reverse:
                prev = next_group
                p = group_start
                while p != next_group:
                    temp = p.next
                    p.next = prev
                    prev = p
                    p = temp
                if prev_end is None:
                    self.head = group_end
                else:
                    prev_end.next = group_end
                prev_end = group_start
                curr = next_group
            else:
                prev_end = group_end
                curr = next_group

            is_reverse = not is_reverse


print(" *** Ant Army ***")
ini_data = input("Input : ").split(",")
data = ini_data[0].split(" ")

k = ini_data[1]

L = LinkedList()

for item in data:
    L.insert(item)

print("Before : ", end="")
L.printList()

L.new_order(int(k))

print()

print("After : ", end="")
L.printList()