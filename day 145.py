'''Binary BattlesN teams have come to participate in a competitive coding event called “Binary Battles”. It is a single-elimination tournament consisting of several rounds.

Note: It is known that N is a power of 2.

In one round, each team will be paired up with and compete against one of the other teams. If there are X teams before the start of a round, 2^X matches are held simultaneously during the round between 2^X pairs of teams. The winning team of each match will move on to the next round, while the losing team of each match will be eliminated. There are no ties involved. The next round will then take place in the same format between the remaining teams. The process will continue until only one team remains, which will be declared the overall winner.

The organizers want to find the total time the event will take to complete. It is given that each round spans A minutes, and that there is a break of B minutes between every two rounds (no break after the last round).

For example, consider a case when N=4, A=10 minutes, and that there is a break of B=5 minutes between every two rounds (no break after the last round).

For example, consider a case when N=4, A=10 and B=5. The first round will consist of two matches and will take 10 minutes to complete. Two teams move on to round 2 and the other two get eliminated. Then there is a break of 5 minutes. The two remaining teams compete in round 2, which lasts 10 more minutes. The team that wins is declared the overall winner. Thus the total time taken is 10 + 5 + 10 = 25 minutes.
10 more minutes. The team that wins is declared the overall winner. Thus the total time taken is 10 + 5 + 10 = 25 minutes.

Can you help the organizers determine how long the event will take to finish?

Input Format
The first line of input will contain a single integer T, denoting the number of test cases. Then the test cases follow.
The first and only line of each test case contains three space-separated integers N, A and B.B respectively — the number of teams, the duration of each round and the length of the breaks between rounds.
Output Format
For each test case, output on a new line the time taken in minutes for the whole event to finish.

Constraints
1≤T≤10
2≤N≤220
1≤A≤100
1≤B≤100
N is a power of 2.
2≤N≤220
20
1≤A≤100
≤
100
1≤A≤100
1≤B≤100
N is a power of 2.
B≤100
1≤B≤100
N is a power of 2.
2≤N≤220
20
1≤A≤100
1≤A≤100
1≤B≤100
N is a power of 2.
Output
4
4 10 5
16 30 5
32 45 15
1024 23 9
25
135
285
311
Explanation:
Test case 1: As explained above, the total time the competition will take is 10 + 5 + 10 = 25 minutes.

Test case 2: 
4 rounds will take place. The total time it will take is 
30 + 5 + 30 + 5 + 30 + 5 + 30 = 135 minutes.'''
import math
for i in range(int(input())):
    N,A,B=map(int,input().split())
    k=int(math.log2(N))
    total_time=k*A+(k-1)*B
    print(total_time)