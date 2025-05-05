'''In mathematics, the degree of polynomials in one variable is the highest power of the variable in the algebraic expression with non-zero coefficient.

Chef has a polynomial in one variable x with N terms. The polynomial looks like 
Find the degree of the polynomial.

Note: It is guaranteed that there exists at least one term with non-zero coefficient.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
First line of each test case contains of a single integer N - the number of terms in the polynomial.

Output Format
For each test case, output in a single line, the degree of the polynomial.'''
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    # Start from the last index and find the first non-zero coefficient
    degree = -1
    for i in range(N-1, -1, -1):
        if A[i] != 0:
            degree = i
            break
            
    print(degree)