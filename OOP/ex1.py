class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1  # Store the first coordinate as an instance variable
        self.coor2 = coor2  # Store the second coordinate as an instance variable

    def distance(self):
        x1, y1 = self.coor1  # Unpack the coordinates
        x2, y2 = self.coor2
        # Calculate the distance using the distance formula
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        return distance  # Return the calculated distance
    def slope(self):
        x1, y1 = self.coor1  # Unpack the coordinates
        x2, y2 = self.coor2
        if abs(x2-x1):
            return ((y2-y1)/(x2-x1))
        
coordinate1 = (3, 2)
coordinate2 = (8, 10)

l1 = Line(coordinate1, coordinate2)
distance = l1.distance()
print(f"The distance between {coordinate1} and {coordinate2} is {distance}")
slope = l1.slope()
print(f"The slope between {coordinate1} and {coordinate2} is {slope}")