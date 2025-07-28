class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)

    def push(self, i):
        self.items.append(int(i))
        self.size += 1

    def check(self, a):
        if int(self.items[self.size-1])+int(a) == 5 or int(self.items[self.size-1])+int(a) == 10 or int(self.items[self.size-1])-int(a) == 5 or int(self.items[self.size-1])-int(a) == 10:         
            self.push(a)
            return
        return

print("***Always 5 or 10***")
n = input("Enter Input : ").split(" ");

stack = Stack()
stack.push(n[0])
for i in n[1:]:
    stack.check(i)

print("Output : ",end="")
for i in stack.items:
    print(f"{i}",end=" ")

