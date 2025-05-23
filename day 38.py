'''Watching Movies at 2x
Chef started watching a movie that runs for a total of X minutes.

Chef has decided to watch the first Y minutes of the movie at twice the usual speed as he was warned by his friends that the movie gets interesting only after the first Y minutes.

How long will Chef spend watching the movie in total?

Note: It is guaranteed that Y is even.

Input Format
The first line contains two space separated integers X,Y - as per the problem statement.

Output Format
Print in a single line, an integer denoting the total number of minutes that Chef spends in watching the movie.
Constraints
1≤X,Y≤1000

Y is an even integer.
Subtasks
Subtask #1 (100 points): original constraints

Sample 1:
Input
Output
100 20
90


Sample 2:
Input
Output
50 24
38
 Chef watches at the usual speed, so it takes him 
26 minutes to watch the remaining portion of the movie.

In total, Chef spends 12+26=38
12+26=38 minutes watching the entire movie.'''
# cook your dish here
X,Y=map(int,input().split())
X_speed=Y//2
normal_speed=X-Y
print(X_speed+normal_speed)
