n = 10  # number of Fibonacci numbers to print
a = 0
b = 1
print(a, b, end=' ')
for _ in range(2, n):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
