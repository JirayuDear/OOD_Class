def bubble(data):
    for last in range(len(data)-1, 0, -1):
        swaped = False
        for i in range(last):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swaped = True

        if not swaped:
            break
    return data

inp = list(map(int, input("Enter input: ").split(' ')))

print(*bubble(inp))