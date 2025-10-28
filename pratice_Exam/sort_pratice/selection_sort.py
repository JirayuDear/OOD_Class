def selection_sort(data):
    for last in range(len(data)-1, 0, -1):
        biggest = data[0]
        biggest_i = 0

        for i in range(1, last+1):
            if(data[i]) > biggest:
                biggest = data[i]
                biggest_i = i
            data[last], data[biggest_i] = data[biggest_i], data[last]

    return data

inp = list(map(int, input("Enter input: ").split(' ')))
print(selection_sort(inp))