def Combination(input_list, answer = []):
    def helper(index, current):
        if index == len(input_list):
            if current:
                answer.append(current[:])
            return
            
        current.append(input_list[index])
        helper(index+1, current)
        current.pop()

        helper(index+1, current) 

    helper(0, [])
    return answer


    
data = list(map(int, input("Enter Input: ").split()))
print(f"Output: {Combination(data)}")