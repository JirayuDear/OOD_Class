class hash:
    def __init__(self, table_size, max_collision, threshold):
        self.table_size = table_size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None] * self.table_size
        self.temp_table = [None]
        
        return True 
    def find_numbers_of_data(self):
        numbers = 0
        for i in self.table:
            if i is not None:
                numbers += 1
        return numbers

    @property
    def load_factor(self):
        return ((self.find_numbers_of_data()+1)*100 / self.table_size)
    
    def insert(self, data):
        if self.load_factor > self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
            self.insert(data)
            return

        indexed = data % self.table_size
        
        for i in range(self.max_collision):
            probe_index = (indexed + i**2) % self.table_size
            if self.table[probe_index] is None:
                self.table[probe_index] = data
                return
            print(f"collision number {i + 1} at {probe_index}")
        
        print("****** Max collision - Rehash !!! ******")
        self.rehash()
        self.insert(data)
    
    def internal_insert(self, key, new_size):
        indexed = key % new_size
        for i in range(self.max_collision):
            probe_index = (indexed + i**2) % new_size
            if self.temp_table[probe_index] is None:
                self.temp_table[probe_index] = key 
                return
            print(f"collision number {i + 1} at {probe_index}")

    def rehash(self):
        new_size = self.cal_prime()
        self.temp_table = [None] * new_size
        old_data = [item for item in self.table if item is not None]
        for i in reversed(old_data):
            self.internal_insert(i, new_size)

        self.table_size = new_size
        self.table = self.temp_table

    def print_table(self):
        for i, item in enumerate(self.table):
            print(f"#{i + 1}\t{item}")
        print("----------------------------------------")


print(" ***** Rehashing *****")
inp = input("Enter Input : ").split('/')
ini_tabel, max_collision, threshold = inp[0].split()
data =  [int(item) for item in inp[1].split()]

hashing = hash(int(ini_tabel), int(max_collision), int(threshold))
print("Initial Table :")
hashing.print_table()
for item in data:
    print(f"Add : {item}")
    hashing.insert(item)
    hashing.print_table()