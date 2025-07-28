class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enQueue(self, i):
        self.items.append(i)
        self.size += 1

    def deQueue(self):
        self.size -= 1
        return self.items.pop(0)

    def check(self, data):
        if "E" in data:
            data = data.replace("E ", "")    
            self.enQueue(data)
            print(self.size)
        if "D" in data:
            if self.items:
                data = data.replace("D ", "")    
                print(f"{self.deQueue()} 0")
            else:
                print(-1)

data = input("Enter Input : ").split(",")
q = Queue()
for i in data:
    q.check(i)
if q.items != []:
    for i in q.items:
        print(i,end=" ")
else:
    print("Empty")
