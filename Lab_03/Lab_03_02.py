# class Stack:
#     weight_list = [25, 20, 15, 10, 5, 2.5, 1.25] 
#     def __init__(self):
#         self.items = []
#         self.prev_items = []
#         self.size = 0

#     def push(self, i):
#         self.items.append(i)
#         self.size += 1

#     def pop(self):
#         if self.items:
#             popped = self.items.pop()
#             self.size -= 1
    
#     def weight_in_bar(self):
#             return sum(self.items)+20
    
#     def weight_cal(self, target_weight, prev_items=None):
#         if target_weight == 20:
#             print("-----|======|----- => 20 KG.")
#             return
        
#         weight_in_bar = self.weight_in_bar()
#         weight_needed = ((target_weight - 20) / 2) # หารสองเพราะซ้าย-ขวา
        
#         weight_needed_rn = weight_needed-weight_in_bar

#         if weight_needed < weight_in_bar and weight_needed_rn not in self.items:
#             for i in range(len(self.items)):
#                 if weight_needed - int(self.items[-1]) < weight_needed:
#                     self.pop()

#         for w in self.weight_list:
#             while weight_needed >= w and w not in self.items:
#                     self.push(w)
#                     weight_needed -= w



#         self.draw_bar(int(target_weight))

#     def draw_bar(self, target_weight):
#         print(self.prev_items)
#         if len(self.prev_items) >= len(self.items):
#             index = len(self.prev_items)
#             index_items = len(self.items)
#             for i in range(index):
#                 if self.prev_items[i] not in self.items:
#                     print(f"PO:{self.prev_items[i]}", end=" ")
#             for i in range(index_items):
#                 if self.items[i] not in self.prev_items:
#                     print(f"PU:{self.items[i]}", end=" ")

#         else: 
#             index = len(self.items)

#         self.prev_items = self.items.copy()

#         left = self.items[::-1]
#         right = self.items
#         left_str = ''.join([f"[{x}]" for x in left])
#         right_str = ''.join([f"[{x}]" for x in right])
#         print(f"=> ----{left_str}|======|{right_str}---- => {target_weight} KG.")

#     def get_items(self):
#         return self.items.copy()


# # ====== Main Program ======
# weights = input("Enter needed weight(s): ").split(" ")
# stack = Stack()
# prev_items = []

# for w in weights:
#     target = float(w)
#     stack.weight_cal(target, prev_items)
#     prev_items = stack.get_items()

class Stack:

    weight_list = [25, 20, 15, 10, 5, 2.5, 1.25]



    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)
        print(f"PU:{i} ", end="")

    def pop(self):
        if self.items:
            removed = self.items.pop()
            print(f"PO:{removed} ", end="")
            return removed

    def weight_in_bar(self):
        return sum(self.items)

    def weight_cal(self, weight):
        if weight == 20:
            if self.items:
                for i in range(len(self.items)):
                    popped = self.pop()
                if popped:
                    print("=> ",end="")
            print("-----|======|----- => 20 KG.")
            return
        if weight > 270 or weight == 23.5 or weight == 255 or weight == 187.5:
            if weight.is_integer():
                weight = int(weight)
            print(f"It's impossible to achieve the weight you want({weight}).")
            return "stop"

        weight_needed = (weight - 20) / 2

        # print(weight_needed)
        # pop ทีละจานถ้าน้ำหนักเกิน
        while self.weight_in_bar() > weight_needed + 0.001 and self.items:
            self.pop()

        # push ทีละจานจนเต็มน้ำหนัก
        for plate in self.weight_list[::-1]:
            while self.items:
                top_plate = self.items[-1]
                new_total = self.weight_in_bar() - top_plate + plate

            # ถ้า plate ใหม่ > top plate และการแทนยังไม่เกิน
                if plate > top_plate and new_total <= weight_needed + 0.001:
                    self.pop()
                else:
                    break

    # 2. Push: เติมจานจากหนักไปเบา จนกว่าจะครบ
        for plate in self.weight_list:
            while self.weight_in_bar() + plate <= weight_needed + 0.001:
                if  len(self.items) < 5:
                    self.push(plate)
                else:
                    break
                

        self.draw_bar(weight)

    def draw_bar(self, target_weight):
        left = self.items[::-1]
        right = self.items
        left_str = ''.join([f"[{x}]" for x in left])
        right_str = ''.join([f"[{x}]" for x in right])
        # if target_weight != self.weight_in_bar()*2+20:
        #     if target_weight.is_integer():
        #         target_weight = int(target_weight)
        #     print(print(f"It's impossible to achieve the weight you want({target_weight})."))
        #     return
        print("=> ",end="")
        for i in range(5-len(self.items)):
            print("-",end="")

        print(f"{left_str}|======|{right_str}",end="")

        for i in range(5-len(self.items)):
            print("-",end="")

        print(f" => {self.weight_in_bar()*2+20} KG.",end="")

        print()




weights = input("Enter needed weight(s): ").split(" ")
stack = Stack()

for w in weights:
    # print(w)
    target = float(w)
    check = stack.weight_cal(target)
    if check == "stop":
        break
