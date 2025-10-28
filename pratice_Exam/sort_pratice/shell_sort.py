"""
    Donald Shell inc = 1, 2, 4, 8, 16, ... , 2^i
    Hibbard inc = 1, 3, 7, 15, ... , 2^i-1
    Sedgewick inc = 1, 8, 23, 77, 281, ... , (4^i+1)+3 * 2^i + 1
"""


def shell_sort(data, dIncrements):
    for inc in dIncrements:
        for i in range(inc, len(data)):
            i_element = data[i]
            for j in range(i, -1, -inc):
                if data[j-inc] > i_element and j >= inc:
                    data[j] = data[j-inc]

                else:
                    data[j] = i_element
                    break
    return data

inp = list(map(int, input("Enter Input: ").split(' ')))
dIncrements = [5, 3, 1]
print(shell_sort(inp, dIncrements))