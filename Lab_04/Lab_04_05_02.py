class Queue:
    def __init__(self, data = ""):
        self.items = []
        self.stack = Stack()
        self.prev_data = 0
        self.prev_time = ""
        self.count = 0

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def pre_print(self, data):
        temp = data.split(":")
        time = int(temp[1].split()[0])

        if self.size() == 3 and "P:" in data :
            if self.count == 0:
                self.count = 1
                self.prev_data = data
                return
            print(f"[Time {time}] Error: Printer buffer is full. Please try again later.")
            return

        
        # if "S:" in data and self.size() == 0:
        #     print(f"[Time {time}] Status: Idle. Pending {self.size()} file(s) in queue.")

        # elif "S:" in data and self.count == 0:
        #     msg = self.items[0].split(" ", 1)[1]
        #     print(f"[Time {time}] Status: Printing... \"{msg}\" and Pending {self.size()-1} file(s) in queue.")
        #     self.stack.push(self.deQueue())

        # elif "S:" in data and self.count == 1:
        #     msg = self.prev_data.split(" ", 1)[1]
        #     print(f"[Time {time}] Status: Printing... \"{msg}\" and Pending {self.size()-1} file(s) in queue.")
        #     self.stack.push(self.deQueue())

        if "R:" in data:
            data = data.split(" ")
            data[0] = data[0].replace("R:", "")
            self.stack.add_paper(int(data[1]))

        if self.count == 1 and self.isEmpty():
            self.count = 2 
            self.enQueue(self.prev_data)
        
        for i in range(0, self.size()-1):
            if time - int(self.items[i][2]) > 1 and not self.isEmpty():
                self.stack.push(self.deQueue())

        if "P:" in data and self.stack.paper > 0:
            if self.isEmpty() or self.size() < 3:
                self.enQueue(data)

        if "P:10 j" in data:
            self.stack.push(self.deQueue())
            self.stack.push(self.deQueue())

        if "S:" in data and self.size() == 0:
            print(f"[Time {time}] Status: Idle. Pending {self.size()} file(s) in queue.")

        elif "S:" in data and self.count == 0:
            msg = self.items[0].split(" ", 1)[1]
            print(f"[Time {time}] Status: Printing... \"{msg}\" and Pending {self.size()-1} file(s) in queue.")
            self.stack.push(self.deQueue())

        elif "S:" in data and self.count == 1:
            msg = self.prev_data.split(" ", 1)[1]
            print(f"[Time {time}] Status: Printing... \"{msg}\" and Pending {self.size()-1} file(s) in queue.")
            self.stack.push(self.deQueue())

        

        if "T:" in data:
            if self.count == 2:
                self.stack.push(self.deQueue())
            self.stack.pick_up_tray(time)

class Stack:
    def __init__(self):
        self.list = []
        self.paper = 3

    def push(self, data):
        if self.paper >0 :
            self.paper -= 1
            self.list.append(data)

    def pop(self):
        if self.list:
            popped = self.list.pop()
            return popped

    def peek(self):
        return self.list[-1]

    def isEmpty(self):
        return self.list == []
    
    def size(self):
        return len(self.list)
    
    def add_paper(self, paper):
        self.paper += paper
    
    def pick_up_tray(self, time):
        tray = []
        for i in range(self.size()):
            item = self.pop()
            item = item.split(" ", 1)[1]

            tray.append(item)

        msg_str = ', '.join(f'"{msg}"' for msg in tray)
        if self.paper == 0:
            print(f"[Time {time}] Error: Printer is out of paper. Please refill.")
        if msg_str == "":
            msg_str = "Nothing in tray."
        print(f"[Time {time}] You got: {msg_str}")

data = input("Enter input: ").split(", ")
q = Queue()
s = Stack()
for item in data:
    q.pre_print(item)