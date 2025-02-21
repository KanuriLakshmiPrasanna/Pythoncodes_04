# Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).
# n will always be greater than 2
def sum_polygon(n):
	if n>2:
		sum_of_internal_angles=(n-2)*180
		return sum_of_internal_angles
internal_angles=sum_polygon(int(input("Enter no.of sides of polygon:")))
print(internal_angles)

