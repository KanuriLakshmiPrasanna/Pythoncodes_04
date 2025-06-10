'''Adjacent Sum Parity
Chef has an array A of length N.
Chef forms a binary array B of length N using the parity of the sums of adjacent elements in A. Formally,
Bi
=(Ai+Ai+1) % 2B i=(A i+A i+1)%2 for 1≤i≤N−11≤i≤N−1BN=(AN+A1) % 2B N=(A N+A 1)%2Here x%yx%y denotes the remainder obtained when xx is divided by y.

Chef lost the array A and needs your help. Given array B, determine whether there exists any valid array A which could have formed B.

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N — the size of the array A.
The second line of each test case contains N space-separated integers B1,B2,B3..Bn denoting the array B.
Output Format
For each testcase, output YES if there exists a valid array A, NO otherwise.

You can print any character in any case. For example YES, Yes, yEs are all considered same.

Constraints
1≤T≤1000
2≤N≤10 
The sum of N over all test cases do not exceed 3⋅10 5

Sample 1:
Input
Output
4
2
0 0
2
1 0
4
1 0 1 0
3
1 0 0
YES
NO
YES
NO
Explanation:
Test case 1: One such valid array is A=[3,3].

Test case 2: It can be shown that no such arrays exist and are valid.

Test case 3: One such valid array is A=[1,2,4,5].'''
for _ in range(int(input())):
    A_arr=int(input())
    B=list(map(int,input().split()))
    total=sum(B)
    if total%2==0:
        print('YES')
    else:
        print('NO')
