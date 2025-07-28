class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        self.size -= 1
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def first(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return ', '.join(str(item) for item in self.items)

lst = []
print(" ***Queue of Queue of Queue of ...***")
inp = input("Enter Input : ").split(",")
for item in inp:
    temp = item.split(" ")
    if temp[0] == "en":
        if lst == []:
            q = Queue()
            print(temp)
            q.enQueue(temp[1])
            lst.append(q)