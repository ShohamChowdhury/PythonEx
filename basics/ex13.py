# Write a function that computes the 
# volume of a sphere given it's radius
import math
def volume(rad):
    return pi*(rad**3)*(4/3)

pi = math.pi
rad = int(input("insert the radius : "))
print(volume(rad))