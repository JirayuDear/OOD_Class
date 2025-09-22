def insertion_sort(data, answer=None):
    if not data:
        return answer
    number = data.pop(0)
    i = 0
    while i < len(answer) and answer[i] < number:
        i += 1
    answer.insert(i, number)
    if not data:
        print(f"insert {number} at index {i} : {answer} ")
    else:
        print(f"insert {number} at index {i} : {answer} {data}")
    return insertion_sort(data, answer)
    
inp = list(map(int,input("Enter Input : ").split(" ")))
first_list = []
first_list.append(inp.pop(0))
result = insertion_sort(inp, first_list)
print("sorted")
print(result)

