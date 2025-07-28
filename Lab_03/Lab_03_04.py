class Stack:
    def __init__(self):
        self.list = []
        self.count = 0  # จำนวน push ที่เกิดขึ้น
        self.index = 0  # สำหรับเก็บ index push ตามโจทย์
        self.check_print = 0
        self.count_print = 0

    def push(self, data):
        self.list.append(data)
        self.index += 1

    def pop(self):
        if self.list:
            popped = self.list.pop()
            self.index -= 1
            return popped

    def peek(self):
        return self.list[-1]

    def isEmpty(self):
        return self.list == []

    def check(self, number, len_input):
        number = int(number)
        if self.isEmpty():
            print(f"Stack push {len(self.list)} index of {number}")
            self.push(number)
            self.count += 1
            return

        if self.peek() < number :
            popped = self.pop()
            print(f"input[{len(self.list)}]({number}) is greater than input[top of stack]({self.count})")
            # if self.check_print != 1:
            #     print(f"input[{len(self.list)}]({number}) is greater than input[top of stack]({self.count_print})")
            #     self.count_print = 1
            # # else:print(f"input[{len(self.list)}]({number}) is greater than input[top of stack]({len(self.list)+self.check_print})")
            print("Stack pop")
            self.push(number)
            self.output(len_input)
            print(f"Stack push {len(self.list)-1} index of {number}")
            self.count += 1

        elif self.peek() > number:
            print(f"Stack push {len(self.list)} index of {number}")
            self.push(number)
            self.count_print = 0
            self.count += 1

    def output(self, len_input):
        # ปรับขนาด list
        while len(self.list) > len_input:
            self.pop()
        while len(self.list) < len_input:
            self.push(-1)

        reverse = self.list[::-1]

        for i in range(len_input):
            if reverse[i] > self.list[i]:
                save = reverse[i]
                self.check_print = 1
                break
        if self.check_print and self.list.index(save) > 3:
            for i in range(self.list.index(save)):
                self.list[i] = int(-1)

        # while self.list[0] != save:
        #     print(f"input[{len(self.list)}]({save}) is greater than input[top of stack]({round_check})")
        
        print(f"Output: {self.list}")
        while len(self.list) > self.count + 1:
            self.pop()

print("*****Big leg on the right side*****")
user_input = input("Enter input: ").split(" ")
len_input = len(user_input)
stack = Stack()
for i in user_input:
    stack.check(i, len_input)

stack.output(len_input)




