
#To calculate circumference of a circle using oops concept
class Circle:
    def __init__(self):
        pi=3.14
        radius=int(input("Enter Radius of circle:"))
        self.pi_value=pi
        self.radius_value=radius
        
        print("Area of circle is",(self.pi_value)*(self.radius_value)**2)
    def circum(self):
        print("Circumference of circle is",2*(self.pi_value)*(self.radius_value) )
circle1_calc=Circle()
circle1_calc.circum()