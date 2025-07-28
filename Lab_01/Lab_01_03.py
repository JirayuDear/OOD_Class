print("*** Reading E-Book ***")
print("Text , Highlight : ",end="")

data = input().split(",")

string = list(data[0])

for i in range(len(string)):
    if string[i] == data[1]:
        string[i]= f"[{data[1]}]"

print("".join(string))