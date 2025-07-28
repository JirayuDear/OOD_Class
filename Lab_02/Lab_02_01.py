class Calculator :
    def __init__(self, x):
        self.x = x
    ### Enter Your Code Here ###

    def __add__(self, y):
        return self.x + y.x
        ###Enter Your Code For Add Number###

    def __sub__(self, y):
        return self.x - y.x
        ###Enter Your Code For Sub Number### 

    def __mul__(self, y):
        return self.x * y.x
        ###Enter Your Code For Mul Number###

    def __truediv__(self, y):
        return self.x / y.x
        ###Enter Your Code For Div Number###

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")
