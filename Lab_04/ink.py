class Queue:
    def __init__(self, data = ""):
        self.items = []
        if data != "":
            self.items.append(data)
        self.size = 0
        self.count = 0

    def enQueue(self, i):
        i = i.replace("en ", "")
        if self.isEmpty():
            self.items.append(Queue(i))
            self.size += 1
            return
        
        for queue in self.items:
            for item in queue.items: 
                if item[0] == i[0]:
                    queue.items.append(i)
                    queue.size += 1
                    return
                
        self.items.append(Queue(i))
        self.size += 1
        return

    def deQueue(self):
        self.size -= 1
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def pinnt(self):
        result = []
        for queue in self.items:
            result.append(queue.items)
        return result

    def __str__(self):
        return f"{self.items}"
    
    





        # if "de" in data:
        #     if self.items:
        #         data = data.replace("de ", "")    
        #         print(f"{self.deQueue()} 0")
        #     else:
        #         print(-1)

print("***Queue of Queue of Queue of ...***")
data = input("Enter Input : ").split(",")
q = Queue()
for i in data:
    if "en" in i:
        q.enQueue(i)
        print(f"Enqueued: {i}")
        print(q.pinnt())
# if q.items != []:
#     for i in q.items:
#         print(i,end=" ")
# else:
#     print("Empty")
