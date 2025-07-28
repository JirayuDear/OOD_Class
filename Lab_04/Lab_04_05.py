class Queue:
    def __init__(self, data = ""):
        self.items = []
        self.stack = Stack()
        self.count = 0

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def print_paper(self, data):
        if "P" in data:
            if self.items:
                self.stack.push(self.deQueue())
            data = data.split(" ")
            data_time = data[0].replace("P:", "")
            data_word = data[1]
            if self.isEmpty():
                self.time = data_time
                self.enQueue([data_time,data_word])
                self.count = 0
            elif self.size() < 3 and self.time == data_time:
                self.enQueue([data_time,data_word])
                self.count += 1
            elif self.time != data_time:
                self.count += 1
                self.enQueue([data_time,data_word])
                self.time = data_time                
                # print(self.stack.items)
            else:
                print("Error: Printer buffer is full. Please try again later.")

        if "T" in data:
            data = data.replace("T:", "")
            # print(self.stack.items)
            self.stack.tray(data)

        if "S" in data:
            data = data.replace("S:", "")
            if self.stack.isEmpty():
                print(f"[Time {data}] Status: Idle. Pending {self.size()} file(s) in queue.")
            else:
                print(f"[Time {data}] Status: Printing... \"{self.stack.items[0][1]}\" and Pending {self.size()} file(s) in queue.")
        if "R" in data:
            data = data.split(" ")
            data[0] = data[0].replace("R:", "")
            self.stack.add_paper(int(data[1]))

    
class Stack:
    def __init__(self):
        self.items = []
        self.items_reverse = self.items[::-1]
        self.paper = 2

    def get_items_list(self):
        return self.items

    def isEmpty(self):
        return self.items == []
        
    def push(self,i):
        if self.size() < 3:
            self.paper -= 1
            self.items.append(i)
            return

    def pop(self):
        if self.items:
            popped = self.items.pop()
            return popped
    

    def size(self):
        return int(len(self.items))

    def tray(self, time):
        # print(self.items)
        # print(time)
        message = []
        if self.isEmpty():
            if self.paper == 0 :print(f"[Time {time}] Error: Printer is out of paper. Please refill.")
            print(f"[Time {time}] You got: Nothing in tray.")
            return
        for items in self.items:
            if int(items[0])+1 <= int(time):
                message.append(items[1])

        msg_str = '", "'.join(message)
        print(f'[Time {time}] You got: "{msg_str}"')

    def add_paper(self, paper):
        self.paper += paper
        return


data = input("Enter input: ").split(",")
q = Queue()
s = Stack()
for item in data:
    q.print_paper(item.strip(" "))