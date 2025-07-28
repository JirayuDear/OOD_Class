# สร้าง class Spherical โดยต้อง
# มี function [changeR , findVolume , findArea]
# มี ตัวแปร radius
# pi = 3.1415926535897932384626433832795028841
# หมายเหตุ สำหรับการ ยกกำลัง ให้ใช้ operator **

class Spherical:

    def __init__(self,r):
        self.pi = 3.1415926535897932384626433832795028841
        self.radius = r

    def changeR(self,Radius):
        self.radius = Radius

    def findVolume(self):
        V = (4/3)*self.pi*(self.radius**3)
        return V

    def findArea(self):
        A = 4*self.pi*(self.radius**2)
        return A

    def __str__(self):
        return f"Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()}"

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)