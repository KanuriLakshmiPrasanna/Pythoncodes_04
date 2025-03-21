'''Chefland Games
In Chefland, a tennis game involves 4 referees.
Each referee has to point out whether he considers the ball to be inside limits or outside limits. The ball is considered to be IN if and only if all the referees agree that it was inside limits.

Given the decision of the 4 referees, help Chef determine whether the ball is considered inside limits or not.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line of input containing 4 integers 
R1,R2,R3,R4,R1,R2,R3,R4 denoting the decision of the respective referees.
Here R can be either 0 or 1 where 
0 would denote that the referee considered the ball to be inside limits whereas 
1 denotes that they consider it to be outside limits.

Output Format
For each test case, output IN if the ball is considered to be inside limits by all referees and OUT otherwise.

The checker is case-insensitive so answers like in, In, and IN would be considered the same.

Constraints
1≤T≤20
0<=R1,R2,R3,R4<=10<=R1,R2,R3,R4<=1

Sample 1:
Input
Output
4
1 1 0 0
0 0 0 0
0 0 0 1
1 1 1 1
OUT
IN
OUT
OUT
Explanation:
Test case 1: Referees 1 and 2 do not consider the ball to be IN. Thus, the ball is OUT.

Test case 2: All referees consider the ball to be IN. Thus, the ball is IN.

Test case 3: Referee 4 does not consider the ball to be IN. Thus, the ball is OUT.

Test case 4: No referee considers the ball to be IN. Thus, the ball is OUT.'''
# cook your dish h
for _ in range(int(input())):
    R1,R2,R3,R4=map(int,input().split())
    if R1==0 and R2==0 and R3==0 and R4==0:
        print("In")
    else:
        print("Out")
