'''Sample Test Case 1
3 3 t 7 7
Tuple contents: 3 3 t 7 7
Number of elements: 5'''


# Read the input line and split it into elements
elements = input().split()

# Convert to a tuple
my_tuple = tuple(elements)

# Output the results
print("Tuple contents:", *my_tuple)
print("Number of elements:", len(my_tuple))
