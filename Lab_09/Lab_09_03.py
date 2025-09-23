def insertion_sort(data, number, index, answer=None):
    if not data:
        if index < len(answer) and answer[index] < number:
            return insertion_sort(data, number, index+1, answer)
        answer.insert(index, number)
        print(f"insert {number} at index {index} : {answer}")
        return answer

    if index < len(answer) and answer[index] < number:
        return insertion_sort(data, number, index+1, answer)

    answer.insert(index, number)
    print(f"insert {number} at index {index} : {answer} {data}")

    next_num = data[0]
    return insertion_sort(data[1:], next_num, 0, answer)


inp = list(map(int,input("Enter Input : ").split(" ")))
first_list = []
first_list.append(inp.pop(0))
result = insertion_sort(inp, inp.pop(0),1,first_list)
print("sorted")
print(result)

