'''Second Largest
Three numbers A, B and C are the inputs. Write a program to find second largest among them.

Input Format
The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three integers A, B and C.

Output Format
For each test case, display the second largest among A, B and C, in a new line.

Constraints
1 ≤ T ≤ 1000
1 ≤ A,B,C ≤ 1000000
Sample 1:
Input
Output
3 
120 11 400
10213 312 10
10 3 450
120
312
10'''

for _ in range(int(input())):
    A,B,C=list(map(int,input().split()))
    variables=[A,B,C]
    variables.sort()
    print(variables[-2])