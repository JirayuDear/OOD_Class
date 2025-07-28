class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def get_items_list(self):
        return self.items
        
    def push(self,i):
        self.items.append(i)
        self.size += 1
        return

    def pop(self):
        if self.items:
            popped = self.items.pop()
            self.size -= 1
        return


    def action(self, state):
        if "spawn" in state:
            state = state.replace("spawn ", "")
            print(f"spawn an enemy of {state} HP")
            self.push(int(state))
        if "dmg" in state:
            state = state.replace("dmg ", "")
            state = int(state)
            dmg = state
            count = 0
            if dmg != 0:
                while state >0 and self.items:
                    hp = int(self.items[-1])
                    if (hp - state) <= 0:
                        state -= hp
                        self.pop()
                        count += 1
                    
                    else:
                        hp -= state
                        state -= hp
                        self.items[-1] = hp
                        break

                print(f"deal {dmg} damage, killed {count} enemy")
            else:
                return print("Invalid number")

        if self.items == []:
            print(self.items)
            print()
            return print(">>>> Player Wins <<<<")
        else:
            return print(self.items)


stack = Stack()

input = input("Enter Input : ").split("/")

input_hp = input[0].split(" ")
input_action = input[1].split(",")


if input_hp != ['']:
    for i in input_hp:
        if i != '0':
            stack.push(int(i))

print()
print("start")
print(stack.get_items_list())
for i in input_action:
    print()
    stack.action(i)