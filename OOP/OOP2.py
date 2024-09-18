from math import pi
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi*(self.radius**2)
    def perimeter(self):
        return 2*pi*self.radius
C1 = Circle(22)
print(C1.area())