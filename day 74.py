'''Chef And Operators
Chef has just started Programming, he is in first year of Engineering. Chef is reading about Relational Operators.
Relational Operators are operators which check relationship between two values. Given two numerical values A and B you need to help chef in finding the relationship between them that is,

First one is greater than second or, First one is less than second or, First and second one are equal.
 

Input
First line contains an integer T, which denotes the number of testcases. Each of the T lines contain two integers A and B.

Output
For each line of input produce one line of output. This line contains any one of the relational operators
'<' , '>' , '='.

Constraints

1 ≤ T ≤ 10000 1 ≤ A, B ≤ 1000000001
Sample 1:
Input
Output
3
10 20
20 10
10 10
<
>
=
Explanation:
In this example 1 as 10 is lesser than 20'''
# cook your dish here
for _ in range(int(input())):
    A,B=map(int,input().split())
    if A<B:
        print("<")
    elif A>B:
        print(">")
    else:
        print("=")