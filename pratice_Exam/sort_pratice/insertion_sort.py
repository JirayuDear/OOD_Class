def insertion_sort(data):
    for i in range(1, len(data)):
        i_element = data[i]
        for j in range(i, -1, -1):
            if j > 0 and data[j-1] > i_element:
                data[j] = data[j-1]
            else:
                data[j] = i_element
                break
    return data

inp = list(map(int, input("Enter input: ").split(' ')))
print(insertion_sort(inp))