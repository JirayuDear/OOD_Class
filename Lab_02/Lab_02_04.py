def hbd(year):
    if int(year) % 2 != 0:
        base = year / 2
        base = round(base)-1
        return f"saimai is just 21, in base {int(base)}!"
    else:
        base = year / 2
        return f"saimai is just 20, in base {int(base)}!"
    
year = input("Enter year : ")
print(hbd(int(year)))