class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, table_size, max_collision):
        self.table_size = table_size
        self.max_collision = max_collision
        self.table = [None] * self.table_size
        self.current_items = 0

    def _calculate_hash(self, key):
        ascii_sum = 0
        for char in str(key):
            ascii_sum += ord(char)
        return ascii_sum % self.table_size

    def insert(self, data_item):
        index = self._calculate_hash(data_item.key)
        
        for i in range(self.max_collision):
            probe_index = (index + i*i) % self.table_size
            
            if self.table[probe_index] is None:
                self.table[probe_index] = data_item
                self.current_items += 1
                return
            else:
                print(f"collision number {i + 1} at {probe_index}")
        
        print("Max of collisionChain")

    def print_table(self):
        for i, item in enumerate(self.table):
            print(f"#{i + 1}\t{item}")

print(" ***** Fun with hashing *****")
inp = input("Enter Input : ")
config_part, data_part = inp.split('/')

table_size, max_collision = map(int, config_part.split())
data_items_str = data_part.split(',')

hashing_table = hash(table_size, max_collision)
full_message_displayed = False

for item_str in data_items_str:
    if hashing_table.current_items >= hashing_table.table_size:
        if not full_message_displayed:
            print("This table is full !!!!!!")
            full_message_displayed = True
        break
    
    try:
        key, value = item_str.strip().rsplit(' ', 1)
        data_to_insert = Data(key, value)
        hashing_table.insert(data_to_insert)
        hashing_table.print_table()
        print("---------------------------")
    except ValueError:
        pass