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

    def printList(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.data))
            node = node.next
        return '->'.join(ans)
    
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
        if self.head == None: return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            p.next = p.next.next
            self.size -= 1
        return p.data

    def bubble_sort(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            prev = None
            curr = self.head

            while curr and curr.next:
                if curr.data > curr.next.data:
                    print(f"Swapping {curr.data} and {curr.next.data}")
                    swapped = True
                    nxt = curr.next
                    curr.next = nxt.next
                    nxt.next = curr

                    if prev:       # ถ้าไม่ใช่ node แรก
                        prev.next = nxt
                    else:          # ถ้าเป็น node แรก
                        self.head = nxt

                    prev = nxt
                    print(f"List: {self.printList()}")
                    print()
                else:
                    prev = curr
                    curr = curr.next


L = LinkedList()

print("*****Bubble Sort Linked List*****")
data = list(map(int, input("Enter List: ").split(",")))
print("Input List: ",end="")

for item in data:
    L.insert(item)

L.printList()
print()
print("_______________________________________")
print()
    
L.bubble_sort()