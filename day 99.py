'''It is My Serve
Alice and Bob are playing a game of table tennis where irrespective of the point scored, every player makes 2 consecutive serves before the service changes. Alice makes the first serve of the match. Therefore the first 2 serves will be made by Alice, then the next 2 serves will be made by Bob and so on.Let's consider the following example match for more clarity:

Alice makes the 1st serve.
Let us assume, Bob wins this point. (Score is 0 for Alice and 1 for Bob)
Alice makes the 2nd serve.
Let us assume, Alice wins this point. (Score is 1 for Alice and 1 for Bob)
Bob makes the 3rd serve.
Let us assume, Alice wins this point. (Score is 2 for Alice and 1 for Bob)
Bob makes the 4th serve.
Let us assume, Alice wins this point. (Score is 3 for Alice and 1 for Bob)
Alice makes the 5th serve.
And the game continues
…
…
After the score reaches P and Q for Alice and Bob respectively, both the players forgot whose serve it is. Help them determine whose service it is.

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains two integers P and Q — the score of Alice and Bob respectively.
Output Format
For each test case, determine which player's (Alice or Bob) serve it is.

You may print each character of Alice and Bob in uppercase or lowercase (for example, Bob, BOB, boB will be considered identical).

Constraints
1 ≤ T ≤ 200
0 ≤ P, Q ≤ 10
Sample 1:
Input
Output
4
0 0
0 2
2 2
4 7
Alice
Bob
Alice
Bob
Explanation:
Test Case 1: Since no points have been scored yet, this is the first serve of the match. Alice makes the 1st serve of the match.
Test Case 2: Two points have been scored yet. Thus, it is the third serve of the match. Bob makes the 3rd serve of the match.
Test Case 3: Four points have been scored yet. Thus, it is the fifth serve of the match. Alice makes the 5th serve of the match.
Test Case 4: Eleven points have been scored yet. Thus, it is the twelfth serve of the match. Bob makes the 12th serve of the match.'''

for _ in range(int(input())):
    P,Q=map(int,input().split())
    serve=(P+Q)+1
    if P==0 and Q==0:
        print("Alice")
    elif serve%4==0:
        print("Bob")
    elif ((serve+1)%4==0):
        print("Bob")
    else:
        print("Alice")
