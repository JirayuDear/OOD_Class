print("*** Fun with Drawing ***")
print("Enter input : ",end="")

n = int(input())

for i in range(0,n):
    for j in range(1, n-i):
        print(".",end="")

    print("*", end="")

    for j in range(0,i*2-1):
        print("+", end="")
    if i != 0: print("*", end="")

    for j in range(1, n*2-2-i*2):
        print(".",end="")

    if i!=n-1 :print("*", end="") 

    for j in range(0,i*2-1):
        print("+", end="")
        count = j*2
    if i != 0: print("*", end="")

    for j in range(1, n-i):
        print(".",end="")
    
    if i != n-1 :print()

count = count+1
for i in range(0,n*2-1):
    for j in range(1,i+1):
        print(".",end="")

    if i != 0: print("*", end="")

    if i != 0 and i != n*2-2:
        for j in range(i, count+2):
            print("+",end="")

        print("*", end="")
    
    for j in range(1,i+1):
        print(".",end="")

    count = count-1
    # print(i)



    print()