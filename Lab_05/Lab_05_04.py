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

    def queen_command(self, command):
        check_angry = 0
        value = command.split(" ")[-1]
        if command.startswith('C') and self.queen_limit < 3:
            print("Food carrying mission : ", end="")
            if self.size == 0:
                print("Empty")
                print("The food load is incomplete!")
                print("Queen is angry! ! !")
                self.queen_limit += 1
                check_angry = 1

            carry = int(value)
            p = self.head
            prev = None

            while p != None:
                next_node = p.next 
                if p.data.startswith('W') and carry > 0 :
                    carry -= 2
                    print(p.data, end=" ")
                    if prev is None:
                        self.head = p.next  
                    else:
                        prev.next = p.next  
                    self.size -= 1
                else:
                    prev = p  
                p = next_node
            if carry == 0:
                print()
        
            if carry > 0:
                p = self.head
                prev = None

                while p != None:
                    next_node = p.next 
                    if p.data.startswith('A') and carry > 0:
                        carry -= 5
                        print(p.data, end=" ")
                        if prev is None:
                            self.head = p.next  
                        else:
                            prev.next = p.next  
                        self.size -= 1
                    else:
                        prev = p  
                    p = next_node
                    if p == None:
                        print()
            
            if carry > 0 and check_angry == 0:
                self.queen_limit += 1
                print("The food load is incomplete!")
                print("Queen is angry! ! !")
            
        
        elif command.startswith('F') and self.queen_limit < 3:
            print("Attack mission : ", end="")
            health = int(value)
            p = self.head
            prev = None

            while p != None:
                next_node = p.next 
                if p.data.startswith('A') and health > 0:
                    health -= 10
                    print(p.data, end=" ")
                    if prev is None:
                        self.head = p.next  
                    else:
                        prev.next = p.next 

                    self.size -= 1 
                else:
                    prev = p  
                p = next_node

            if health > 0:
                p = self.head
                prev = None

                while p != None:
                    next_node = p.next 
                    if p.data.startswith('W') and health > 0:
                        health -= 5
                        print(p.data, end=" ")
                        if prev is None:
                            self.head = p.next  
                        else:
                            prev.next = p.next  

                        self.size -= 1
                    else:
                        prev = p  
                    p = next_node
            if health > 0:
                self.queen_limit = 4

            print()

        elif command.startswith('S') and self.queen_limit < 3:
            p = self.head
            count = 0
            print("-> Remaining worker ants: ", end="")
            while p != None: 
                if p.data.startswith('W'):
                    print(p.data, end=" ")
                    count = 1
                p = p.next
                if count == 0 and p == None:
                    print("Empty")
                    count = 1
                    break
                if p == None:
                    print()
            if count == 0:
                print("Empty")
            print("-> Remaining soldier ants: ", end="")
            p = self.head
            count = 0
            while p != None: 
                if p.data.startswith('A'):
                    print(p.data, end=" ")
                    count = 1
                p = p.next
                if count == 0 and p == None:
                    print("Empty")
                    count = 1
                    break
                if p == None:
                    print()
            if count == 0:
                print("Empty")

        elif command.startswith('W') and self.queen_limit < 3:
            for i in range(1,int(value)+1):
                self.insert(f"W{i}")
        elif command.startswith('A') and self.queen_limit < 3:
            for i in range(1,int(value)+1):
                self.insert(f"A{i}")
        
        if self.queen_limit == 4:
            print("Ant nest has fallen!")
            self.queen_limit += 1
            return

        if self.queen_limit == 3:
            print("**The queen is furious! The ant colony has been destroyed**")
            return

print("***This colony is our home***")
data = input("Enter input : ").split(",")
initial = data[0].split("/")
data[0] = initial[1]
initial = initial[0].split(" ")

L = LinkedList()

print("Current Ant List: ", end="")
if int(initial[0]) == 0 and int(initial[1]) == 0:
    print("Empty", end="")
else:
    for j in range(1, int(initial[0])+1):
        L.insert(f"W{j}")
        print(f"W{j}",end=" ")
    for k in range(1, int(initial[1])+1):
        L.insert(f"A{k}")
        print(f"A{k}",end=" ")

print()
print()

for item in data:
    if L.queen_limit != 3:
        L.queen_command(item)



