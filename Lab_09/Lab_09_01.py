def bubble_sort(data):
    n = len(data)
    printed_last = False

    for i in range(n-1):
        moved = None
        for j in range(n-1-i):
            print(data[j])
            if data[j] > data[j+1]:
                moved = data[j]  
                data[j], data[j+1] = data[j+1], data[j]

        if moved is not None:  
            if i < n-2:
                print(f"{i+1} step : {data} move[{moved}]")
            else:
                print(f"last step : {data} move[{moved}]")
                printed_last = True
                break

    if not printed_last:  #
        print(f"last step : {data} move[{None}]")

inp = list(map(int, input("Enter Input : ").split()))
bubble_sort(inp)
