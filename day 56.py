''' Chef Eren
Chef is a very big fan of Eren Yeager.

In the last season of Attack on Titan, there were N episodes numbered from 1 to N.
Each even indexed episode was A minutes long and each odd indexed episode was B minutes long.

Calculate the total duration (in minutes) of the last season.

Input Format
The first line of input contains a single integer T, the number of test cases.
The first and only line of each test case contains three integers N, A, and B, the number of episodes and the durations of each even-indexed and odd-indexed episodes respectively in minutes.

Output Format
For each test case, print a single integer on a new line, the total duration of the last season in minutes.

Constraints
1≤T≤100
1≤N≤60
1≤A,B≤60
Sample 1:
Input
Output
3
1 2 2
2 3 4
4 20 30
2
7
100
Explanation:
Test case 1: There is only one episode, so there is 1 odd-indexed episode, and 0 even-indexed episode. The total duration of the season 
=0⋅A+1⋅B=0⋅2+1⋅2=2.

Test case 2: There are two episodes with indices 
{1,2}. Thus, there is 1 odd-indexed episode({1}), and 1 even-indexed episode ({2}). The total duration of the season =1⋅A+1⋅B=1⋅3+1⋅4=7.

Test case 3: There are four episodes with indices {1,2,3,4}. Thus, there are 2 odd-indexed episodes ({1,3}), and 2 even-indexed episodes ({2,4}). The total duration of the season =2⋅A+2⋅B=2⋅20+2⋅30=100.'''
T = int(input())  # Number of test cases

for _ in range(T):
    N, A, B = map(int, input().split())
    odd_episodes = (N + 1) // 2
    even_episodes = N // 2
    total_time = (odd_episodes * B) + (even_episodes * A)
    print(total_time)
