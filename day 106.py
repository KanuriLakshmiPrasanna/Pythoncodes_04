''' Minimum number of Flips
Chef has an array A of length N consisting of 1 and -1 only.

In one operation, Chef can choose any index i (1≤i≤N) and multiply the element A[i] by -1.

Find the minimum number of operations required to make the sum of the array equal to 0. Output -1 if the sum of the array cannot be made 0.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
First line of each test case consists of a single integer N denoting the length of the array.
Second line of each test case contains N space-separated integers A1, A2, …, AN denoting the array A.
Output Format
For each test case, output the minimum number of operations to make the sum of the array equal to 0. Output -1 if it is not possible to make the sum equal to 0.

Constraints
1≤T≤100
2≤N≤1000
Ai=1 or Ai=−1
Sample 1:
Input
Output
4
4
1 1 1 1
5
1 -1 1 -1 1
6
1 -1 -1 1 1 1
2
1 -1
2
-1
1
0
Explanation:
Test case 1: The minimum number of operations required is 2. In the first operation, change A3 from 1 to -1. Similarly, in the second operation, change A4 from 1 to -1. Thus, the sum of the final array is 1+1−1−1=0.

Test case 2: It can be proven that the sum of the array cannot be made equal to zero by making any number of operations.

Test case 3: We can change A1 from 1 to -1 in one operation. Thus, the sum of the array becomes −1−1−1+1+1+1=0.

Test case 4: The sum of the array is already zero. Thus we do not need to make any operations.'''
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    cnt1 = A.count(1)
    cnt_1 = A.count(-1)
    total_sum = cnt1 - cnt_1

    if total_sum % 2 != 0:
        print(-1)
    else:
        print(abs(total_sum) // 2)
