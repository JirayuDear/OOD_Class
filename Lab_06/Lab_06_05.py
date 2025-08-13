def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def find_total_weight_of_one(purify, weight):
    if purify == 1: return weight
    
    ck = fib(purify - 1)

    x = 2 * weight + 1 - ck
    total_ab = x

    if total_ab < 2: return -1
    
    if total_ab % 2 == 0:
        a = b = total_ab // 2
    else:
        a = total_ab // 2
        b = total_ab - a

    wa = find_total_weight_of_one(purify - 1, a)
    wb = find_total_weight_of_one(purify - 1, b)
    
    return wa + wb

data = list(map(int, input("Purity and Weight needed: ").split()))
result = find_total_weight_of_one(data[0], data[1])
print(f"Total weight of used minerals with Purity 1 : {result}")
