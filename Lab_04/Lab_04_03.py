class Queue:
    def __init__(self, init_list = []):
        self.list = init_list
        self.size = 0
    
    def enqueue(self,data):
        self.list.append(data)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.list.pop(0)

    def pop(self):
        self.size -= 1
        return self.list.pop()
        
    def peek(self): #ใช้ดูตัวแรกของ Queue
        return self.list[-1]
    
    @property
    def len_size(self):
        return len(self.list)
    
    def hot_potato(self, data_ppl, data_round):
        for i in data_ppl:
            self.enqueue(i)
        while self.size != 1:
            for i in range(0, data_round+1):
                if i == 0 and self.list:
                    pop = self.dequeue()
                    print(f"{pop} is the first player holding the potato")
                    self.enqueue(pop)
                # print(self.list)
                elif self.list:
                    pop = self.dequeue()
                    print(f"  Potato passed to: {pop}")
                    self.enqueue(pop)
                # print(self.list)
            print(f"Eliminated: {self.peek()}.",end=" ") 
            self.pop()
            print(f"Remaining players: {self.list}")
        
        print()
        print(f"The winner is: {self.dequeue()}!")


            

    
    def __str__(self):
        return str(self.list)
    
    
print("*****Hot Potato Game*****")
data = input("Enter Input: ").split("/")
data_ppl = list(data[0].split(","))
data_round = int(data[1])

q = Queue()
q.hot_potato(data_ppl,data_round)