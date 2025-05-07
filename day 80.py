'''
You're given two integers A and B. You need to output their sum.
The first line contains an integer T, the number of test cases.

Each test case consists of two integers A and B.
input
3
1 2
100 200
10 40

output
3
300
50
'''
# Number of test cases
T = int(input())

for _ in range(T):
    # Read two integers A and B
    A, B = map(int, input().split())
    # Print their sum
    print(A + B)