class Queue:
    def __init__(self, data = ""):
        self.items = []
        if data != "":
            self.items.append(data)
        self.size = 0
        self.count = 0

    def enQueue(self, i):
        self.items.append(i)
        self.size += 1

    def deQueue(self):
        self.size -= 1
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def __str__(self):
        return "[" + ", ".join(str(item) for item in self.items) + "]"
    
    def check(self, i):
        if "en" in i:
            i = i.replace("en ", "")
            if self.isEmpty():
                self.enQueue(Queue(i))
                print(f"Enqueued: {i}")
                return
        
            for queue in self.items:
                for item in queue.items: 
                    if item[0] == i[0]:
                        queue.enQueue(i)
                        print(f"Enqueued: {i}")
                        return
                
            self.enQueue(Queue(i))
            print(f"Enqueued: {i}")
            self.size += 1
            return
        if "de" in i:
            for queue in self.items:
                if queue.items:
                    print(f"Dequeued: {queue.deQueue()}")
                    print(self.pinnt())
                    if queue.items == []:
                        self.deQueue()
                    return
            if self.items == []:
                print("Queue is empty")
            
                
    def pinnt(self):
        self.result = []
        for queue in self.items:
            self.result.append(queue.items)
        return f"Queue state: {[[int(j) for j in i ]for i in self.result if i != []]}"

print(" ***Queue of Queue of Queue of ...***")
data = input("Enter Input : ").split(",")
q = Queue()
for i in data:
    if "en" in i:
        q.check(i)
        print(q.pinnt())
    if "de" in i:
        q.check(i)