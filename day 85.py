'''Chefs maths teacher wants to check his ability to find out the prime numbers in a given list. Help hik to find the prime numbers of given list
NOTE: Prime numbers are those numbers which are only divisible by 1 and the number itself'''
# Get numbers from the user as input
numbers = input("Enter numbers separated by spaces: ").split()

# Convert input strings to integers
numbers = [int(num) for num in numbers]

# Find and print prime numbers
print("Prime numbers in the list:")
for num in numbers:
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
