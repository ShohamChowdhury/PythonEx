class Cylinder:
    def __init__(self,height=1,radius=1):
        self.radius = int(radius)
        self.height = int(height)
    def volume(self):
        print(3.1416*(self.radius**2)*self.height)
    def surface_area(self):
        print(2*3.1416*self.radius*(self.radius+self.height))
c = Cylinder(2,3)
c.surface_area()
c.volume()
        