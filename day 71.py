'''Dracula Eats
Eat, drink, and be scary

There are N spooky days left until Halloween.
Dracula dines at a mysterious restaurant that changes its spooky menu daily. He particularly enjoys what they serve on Tuesday.

Today is Monday, so he wishes to calculate how many times he can indulge in his favourite menu in the next N days (including today) before Halloween.

Note that Dracula follows the standard 7-day calendar, with Tuesday immediately following Monday.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
The only line of each test case contains a single integer N, denoting the number of spooky days.
Output Format
For each test case, output on a new line the number of times Dracula would have had his favorite meal after N days.

Constraints
1≤T≤1000
1≤N≤1000
Sample 1:
Input
Output
4
1
10
15
16
0
2
2
3
Explanation:
Test case 1: The first day is Monday, and Dracula has only one day. So, no Tuesdays are encountered, and the answer is 0.

Test case 2: The first day is Monday, so the second and ninth days are Tuesdays.
Dracula can eat his favorite meal twice.

Test case 3: Once again, the second and ninth days are Tuesday, so in 15 days, Dracula still gets to eat his favorite meal only twice.

Test case 4: After the ninth day, the 16-th day is also a Tuesday. So, this time Dracula gets to eat his favorite meal three times - on days 2,9,16.'''

T = int(input())  # Number of test cases

for _ in range(T):
    N = int(input())  # Number of spooky days
    count = 0
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for i in range(N):  # i from 0 to N-1
        current_day = day_of_week[i % 7]
        if current_day == "Tuesday":
            count += 1

    print(count)