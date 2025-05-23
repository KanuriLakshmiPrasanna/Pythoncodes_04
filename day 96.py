'''Small factorials
You are asked to calculate factorials of some small positive integers.

Input
An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1 <= n <= 100

Output
For each integer n given at input, display a line with the value of n!

Note: For larger numbers, their factorial can overflows any available numeric data type in C.

Sample 1:
Input
Output
4
1
2
5
3
1
2
120
6 '''

for _ in range(int(input())):
    n=int(input())
    result=1
    for i in range(1,n+1):
        result*=i
    print(result)