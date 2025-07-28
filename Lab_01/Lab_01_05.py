def max(data):
    max_value = 0
    temp = 0
    for i in data:
        if int(i) > int((max_value)):
            temp = max_value
            max_value = i
        elif int(i) > int(temp):
            temp = i
    return max_value, temp



def vickrey(data):

    if len(data) <=1:
        print("not enough bidder")
        return

    max_value, almost_max = max(data)

    if max_value != almost_max: 
        print(f"winner bid is {max_value} need to pay {almost_max}")
    elif max_value == almost_max:
        print("error : have more than one highest bid")

    return


print("Enter All Bid : ",end="")
data = input().split(" ")
vickrey(data)

