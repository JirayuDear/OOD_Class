class Stack :
    def __init__(self):
        self.items = []
        self.result = ""
        self.size = 0

    def push(self, i):
        self.items.append(i)
        self.size += 1

    def get_items_list(self):
        return self.items
    
    def list_to_str(self):
        for i in self.items:
            if self.items.index(i) != len(self.items)-1:
                self.result = self.result+str(i)
        self.result = self.result[::-1]
            
        return int(self.result)

    
def dec2bin(decnum):

    s = Stack()
    while (decnum > 0 ):
        remainder = decnum % 2
        s.push(remainder)
        decnum = decnum // 2

    if decnum == 0: 
        s.push(0) 
    else: s.push(1)

    return s.list_to_str()

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))