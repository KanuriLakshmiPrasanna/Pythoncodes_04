#To calculate the circumference of circle using Oops Methods

class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=2*self.pi*radius
    def circumference(self):
        return 2*self.pi*self.radius
circle_1=Circle(5)
print(f"Circumference of circle is {circle_1.circumference()}")
print(f"Area of circle is {circle_1.area}")
