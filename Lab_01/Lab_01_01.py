print("*** Rabbit & Turtle ***")
print("Enter Input : ",end = "")

data = input().split(' ')

t  = int(data[0])/(int(data[2])-int(data[1]))
answer = int(data[3]) * t

print(f"{answer:.2f}")
