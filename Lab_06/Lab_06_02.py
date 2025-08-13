def sort_list(data, index, bubble_sort_period = 0):
    if index < len(data)-1 and data[index] < data[index+1]:
        temp = data[index]
        data[index] = data[index+1]
        data[index+1] = temp
    if bubble_sort_period > len(data):
        return data
    if index > len(data):
        bubble_sort_period += 1
        index = 0
        sort_list(data, index, bubble_sort_period)
    return sort_list(data, index+1, bubble_sort_period)

data = list(map(int, input("Enter your List : ").split(',')))
print(f"List after Sorted : {sort_list(data, 0)}")