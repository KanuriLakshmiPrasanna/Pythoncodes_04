'''Decrement OR Increment
Write a program to obtain a number N and increment its value by 1 if the number is divisible by 4 otherwise decrement its value by 1.

Input Format
First line will contain a number N.

Output Format
Output a single line, the new value of the number.

Constraints
0≤N≤1000

Sample 1:
Input
Output
5
4
Explanation:
Since 5 is not divisible by 4 hence, its value is decreased by 1.'''
# cook your dish here
N=int(input())
if N%4==0:
    print(N+1)
else:
    print(N-1)