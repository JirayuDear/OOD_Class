def find_min(data, index, min_number):
    if index > len(data)-1: return min_number
    if data[index] <= min_number:
        min_number = data[index]
    return find_min(data, index+1, min_number)

data = list(map(int, input('Enter Input : ').split(" ")))
print(f"Min : {find_min(data, 0, data[0])}")
