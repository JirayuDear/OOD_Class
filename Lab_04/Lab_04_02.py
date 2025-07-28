class Queue:
    def __init__(self):
        self.items = []
        self.A = []
        self.B = []
        self.size = 0

    def enQueue(self, i):
        self.items.append(i)
        self.size += 1

    def deQueue(self):
        self.size -= 1
        return self.items.pop(0)
    
    def wait_row(self, data_ppl, data_mn):
        for i in data_ppl:
            self.enQueue(i)
        for i in range(1,data_mn+1):
            print(i,end=" ") 
            if i % 3 == 1 and self.A and i != 1:
                self.A.pop(0)
            if i % 2 == 0 and self.B:
                self.B.pop(0) 
            if self.items:
                if len(self.A) < 5:
                    self.A.append(self.deQueue())
                elif len(self.B) < 5:
                    self.B.append(self.deQueue())
            # if i % 3 == 1 and self.A and i != 1:
            #     self.A.pop(0)
            # if i % 2 == 0 and self.B:
            #     self.B.pop(0)
            print(f"{self.items}",end=" ")
            print(f"{self.A}",end = " ")
            print(f"{self.B}")
            

data = input("Enter people and time : ").split(" ")

q = Queue()
q.wait_row(data[0], int(data[1]))
