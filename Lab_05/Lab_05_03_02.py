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

    def check_same_repo(self):
        p = self.head
        while p != None:
            if p.next != None and p.next.data == "|":
                if self.prev_repo == 0:
                    self.prev_repo = p.data
                elif self.prev_repo == p.data:
                    self.prev_repo = p.data
                    self.same_repo = True
                else: 
                    self.prev_repo = p.data
                    self.same_repo = False
                    break
            p = p.next
        print(f"Are these branches in the same repository? {self.same_repo}")
        if not self.same_repo:
            return
        return self.check_merge()

    def check_merge(self, link_list, my_index):
        p = self.head                   
        merge = 0            

        for i in range(my_index, len(link_list)):
            if i == my_index:
                continue
            if self.head.data == link_list[i].head.data:
                return merge

            p = self.head
            prev_A = p
            prev_B = p.next    

            while prev_B is not None:
                t = link_list[i].head
                while t is not None and t.next is not None:
                    if prev_B.data == t.next.data and prev_A.data != t.data:
                        check = True
                        c = counted.head
                        while c is not None:
                            if prev_B.data == c.data:
                                check = False
                                break
                            c = c.next

                        if check:
                            counted.insert(prev_B.data)
                            merge += 1

                    t = t.next
                p = p.next
                prev_A = p
                prev_B = p.next
        return merge

    def get_tail(self):
        p = self.head
        while p != None:
            if p.next == None:
                return p.data
            p = p.next

    def get_head(self):
        return self.head

data = input("Git History: ").split("|")
new_data = []
for item in data:
    new_data.append(item.split(" -> "))
# print(new_data)

link_list = []
same_repo = False
merge = 0

for item in new_data:
    L = LinkedList()
    for i in item:
        L.insert(i.strip(" "))
    link_list.append(L)
    
# L.check_same_repo()
counted = LinkedList()

def check_repo():
    for i in range(len(link_list)-1):
        if link_list[i].get_tail() == link_list[i+1].get_tail():
            same_repo = True
        else: 
            same_repo = False
            return same_repo
        return same_repo
    
print(f"Are these branches in the same repository? {check_repo()}")

if check_repo():
    for i in range(len(link_list)):
        merge += link_list[i].check_merge(link_list, i)
    print(f"{merge} Merge(s)")
