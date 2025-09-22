def sort_by_number(data):
    result = []
    checked = []
    for num in data:
        if num not in checked:
            count = 0
            for x in data:
                if x == num:
                    count += 1
            result.append([count, num])
            checked.append(num)
    return result


inp = list(map(int, input("Enter list  of numbers: ").split()))

result = sort_by_number(inp)            
while result:
    max_pair = result[0]
    for pair in result[1:]:
        if pair[0] > max_pair[0]:
            max_pair = pair
        elif pair[0] == max_pair[0]:
            if inp.index(pair[1]) < inp.index(max_pair[1]):
                max_pair = pair

    print(f"number {max_pair[1]}, total: {max_pair[0]}")
    result.remove(max_pair)