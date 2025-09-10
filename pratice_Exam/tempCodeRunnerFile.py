                    if prev:       # ถ้าไม่ใช่ node แรก
                        prev.next = nxt
                    else:          # ถ้าเป็น node แรก
                        self.head = nxt
                
                    prev = nxt
                    # print(f"List: {self.printList()}")