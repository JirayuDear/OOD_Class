def sort_by_alphabet(data):
    temp = []
    answer = []
    for i in data:
        for j in i:
            if j.isalpha():
                temp.append(j)
    for i in range(len(temp)-1):
        for j in range(len(temp)-i-1):
            if temp[j+1] < temp[j]:
                a = temp[j]
                temp[j] = temp[j+1]
                temp[j+1] = a

    for i in temp:
        for j in data:
            if i in j:
                answer.append(j)

    return answer

inp = input("Enter Input : ").split(" ")
result = sort_by_alphabet(inp)
for i in result:
    print(i, end=" ")