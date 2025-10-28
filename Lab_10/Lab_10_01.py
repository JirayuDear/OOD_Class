def cal_percentile(data, index):
    n = len(data)
    if index == 999:
        return 100
    percentile = float((index + 1)*100/n)
    if percentile == 0 or percentile == 100:
        return int(percentile)
    return percentile


def binary_search(data, value):
    #index
    low = 0
    high = len(data)-1
    if value < data[0]:
        return -1
    if value > data[-1]:
        return 999
    while(low<=high):
        mid = int((low+high)/2)
        if data[mid] == value:
            return float(mid)
        elif data[mid] < value:
            low = mid+1
        elif data[mid] > value:
            high = mid-1

    lower_index = high
    upper_index = low
    
    value_lower = data[lower_index]
    value_upper = data[upper_index]
    

    decimal = (value - value_lower) / (value_upper - value_lower)
    index = (upper_index - lower_index) * decimal + lower_index
    
    return index


inp = input("Enter Input : ").split("/")
data =  [float(i) for i in inp[0].strip().split(" ")]
percentile = int(inp[1])
index = binary_search(data, percentile)
print()
print(f"index      :   {index}")
print(f"percentile :   {cal_percentile(data, index)}")

