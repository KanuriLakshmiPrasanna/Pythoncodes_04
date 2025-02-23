#Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.
def next_edge(side1, side2):
		max_range_of_side_3=(side1+side2-1)
		return max_range_of_side_3

side1=int(input("Enter length of side1:"))
side2=int(input("Enter length of side2:"))
side3=next_edge(side1,side2)
print(f"Max range of a triangles third edge {side3}")