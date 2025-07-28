class Stack:
    def __init__(self):
        self.stack = []

    def check(self, input_list):
        n = len(input_list)
        self.result = [-1] * n

        for i in range(n):
            while self.stack and input_list[i] > input_list[self.stack[-1]]:
                idx = self.stack.pop()
                print(f"input[{i}]({input_list[i]}) is greater than input[top of stack]({input_list[idx]})")
                print("Stack pop")
                self.result[idx] = input_list[i]
                self.output()

            # Push เสมอหลังเปรียบเทียบ
            self.stack.append(i)
            print(f"Stack push {i} index of {input_list[i]}")
            if i == n-1:
                self.output()

    def output(self):
        print(f"Output: {self.result}")


print("*****Big leg on the right side*****")
user_input = list(map(int, input("Enter input: ").split(" ")))
stack = Stack()
stack.check(user_input)
