def can_pack(capacity, weights, k):
    if max(weights) > capacity:
        return False

    boxes_used = 1
    current_weight = 0

    for weight in weights:
        if current_weight + weight <= capacity:
            current_weight += weight
        else:
            boxes_used += 1
            current_weight = weight
    
    return boxes_used <= k

def solve():
    inp_str = input("Enter Input : ")
    weights_str, k_str = inp_str.split('/')
    
    weights = list(map(int, weights_str.split()))
    k = int(k_str)

    low = max(weights) 
    high = sum(weights) 
    min_capacity = high

    while low <= high:
        mid = (low + high) // 2
        
        if can_pack(mid, weights, k):
            min_capacity = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(f"Minimum weigth for {k} box(es) = {min_capacity}")
solve()