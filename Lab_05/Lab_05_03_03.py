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
        # self.counted = None
        self.prev_repo = 0
        self.same_repo = False
        self.merge = 0
        self.size = 0
        self.zero = 0
        self.prev_A = 0
        self.prev_B = 0

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

    def get_tail(self):
        p = self.head
        while p != None:
            if p.next == None:
                return p.data
            p = p.next

    def check_merge(self, link_list, my_index, counted):
        merge = 0
        p = self.head

        while p != None and p.next != None:
            current_data = p.data

            if p.next == None:
                break

            for i in range(len(link_list)):
                if i == my_index:
                    continue

                q = link_list[i].head
                while q != None and q.next != None:
                    if q.data == current_data and q.next.data != p.next.data:
                        r = counted.head
                        already_counted = False
                        while r != None:
                            if r.data == q.data:
                                already_counted = True
                                break
                            r = r.next
                        if not already_counted:
                            merge += 1
                            counted.insert(current_data)
                    q = q.next
            p = p.next

        return merge



data = input("Git History: ").split("|")
new_data = []
for item in data:
    new_data.append(item.split(" -> "))

link_list = []
same_repo = False
merge = 0

for item in new_data:
    L = LinkedList()
    for i in item:
        L.insert(i.strip(" "))
    link_list.append(L)
    
counted = LinkedList()

def check_repo():
    for i in range(len(link_list)-1):
        if link_list[i].get_tail() != link_list[i+1].get_tail():
            return False
    return True
print(f"Are these branches in the same repository? {check_repo()}")

if check_repo():
    for i in range(len(link_list)):
        merge += link_list[i].check_merge(link_list, i, counted)
    print(f"{merge} Merge(s)")