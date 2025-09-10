class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert(self, data):
        p = Node(data)
        if self.head is None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.size += 1