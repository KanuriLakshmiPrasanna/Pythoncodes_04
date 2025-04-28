'''Small Factorial
Write a program to find the factorial value of any number entered by the user.

Input Format
The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains an integer N.

Output Format
For each test case, display the factorial of the given number N in a new line.

Constraints
1 ≤ T ≤ 1000
0 ≤ N ≤ 20
Sample 1:
Input
Output
3 
3 
4
5
6
24
120'''
for _ in range(int(input())):
    N=int(input())
    result=1
    for i in range(1,N+1):
        result*=i
    print(result)