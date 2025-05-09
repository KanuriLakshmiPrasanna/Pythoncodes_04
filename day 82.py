'''Chefia wants to build a caculator for simple operations like additions subractions multiplications and divisions help her to build the simple caculator which takes input from user'''

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero.")
else:
    print("Invalid operator.")

