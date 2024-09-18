pi = 22 / 7


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(pi * pow(self.radius, 2))

    def perimeter(self):
        print(2 * pi * self.radius)


c1 = Circle(int(input("Please enter Radius :\n")))
print("Area of the circle is : ")
c1.area()
print("Perimeter of the circle is : ")
c1.perimeter()
