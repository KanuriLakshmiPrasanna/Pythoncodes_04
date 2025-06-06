'''Possible Victory
Chef is playing in a T20 cricket match. In a match, Team A plays for 20 overs. In a single over, the team gets to play 6 times, and in each of these 6 tries, they can score a maximum of 6 runs. After Team A's 20 overs are finished, Team B similarly plays for 20 overs and tries to get a higher total score than the first team. The team with the higher total score at the end wins the match.

Chef is in Team B. Team A has already played their 20 overs, and have gotten a score of R. Chef's Team B has started playing, and have already scored C runs in the first O overs. In the remaining 20−O overs, find whether it is possible for Chef's Team B to get a score high enough to win the game. That is, can their final score be strictly larger than R?

Input Format
There is a single line of input, with three integers, R,O,C.
Output Format
Output in a single line, the answer, which should be "YES" if it's possible for Chef's Team B to win the match and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Constraints
0≤C≤R≤720
1≤O≤19
0≤C≤36∗O
Sample 1:
Input
Output
719 18 648
YES
Explanation:
In the remaining 
20−O=2 overs, Team B gets to play 
2∗6=12 times, and in each try, they can get a maximum of 6 score. Which means that the maximum score that they can acheieve in these 2 overs is 
12∗6=72. Thus, the maximum total score that Team B can achieve is C+72=720. 720 is strictly more than Team A's score of 719, and hence Chef's Team B can win this match.

Sample 2:
Input
Output
720 18 648
NO
Explanation:
Similar to the previous explanation, the maximum total score that Team B can achieve is 720, which isn't strictly greater than Team A's 720.Hence Chef's Team B can't win this match.'''

# cook your dish here
R,O,C=map(int,input().split())
overs_left=20-O
if O<20:
    balls_left=overs_left*6
    max_score=balls_left*6
    if max_score>(R-C):
        print("Yes")
    else:
        print("No")