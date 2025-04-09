''' Chessboard Distance
The Chessboard Distance for any two points 

Input Format
First line will contain T, the number of test cases. Then the test cases follow.
Each test case consists of a single line of input containing 4 space separated integers - 
as defined in the problem statement.
Output Format
For each test case, output in a single line the chessboard distance between 
Constraints
1≤T≤1000
 
Subtasks
Subtask #1 (100 points): original constraints

Sample 1:
Input
Output
3
2 4 5 1
5 5 5 3
1 4 3 3
3
2
2
Explanation:
In the first case, the distance between 
max(∣2−5∣,∣4−1∣)=max(∣−3∣,∣3∣)=3.

In the second case, the distance between 
max(∣5−5∣,∣5−3∣)=max(∣0∣,∣2∣)=2.

In the third case, the distance between 
max(∣1−3∣,∣4−3∣)=max(∣−2∣,∣1∣)=2.'''

for _ in range(int(input())):
    X1,Y1,X2,Y2=map(int,input().split())
    distance=max(abs(X1-X2),abs(Y1-Y2))
    print(distance)
