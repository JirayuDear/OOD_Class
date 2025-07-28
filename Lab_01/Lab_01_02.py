print("*** multiplication or sum ***")
print("Enter num1 num2 : ",end="")

data = input().split(" ")

if int(data[0]) * int(data[1]) > 1000:
    print("The result is ",end="")
    print(int(data[0]) + int(data[1]))

if int(data[0]) * int(data[1])  <= 1000:
    print("The result is ",end="")
    print(int(data[0]) * int(data[1]))