#Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

from math import pi
def radians_to_degrees(rad):
    degree=rad*180/pi
    return degree
    
    
rad=int(input("Enter Radian:"))
result=radians_to_degrees(rad)
print(round(result,1))