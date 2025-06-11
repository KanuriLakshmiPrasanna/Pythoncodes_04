''' Candies
Abhi is a salesman. He was given two types of candies, which he is selling in N different cities.

For the prices of the candies to be valid, Abhi's boss laid down the following condition:

A given type of candy must have distinct prices in all N cities.
In his excitement, Abhi wrote down the prices of both the candies on the same page and in random order instead of writing them on different pages. Now he is asking for your help to find out if the prices he wrote are valid or not.

You are given an array A of size 2N. Find out whether it is possible to split A into two arrays, each of length N, such that both arrays consist of distinct elements.

Both arrays can have distinct elements only if no element in the original array is repeated more than twice.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains one integer N, denoting the number of cities
The second line contains 2N space-separated integers A1,A2....An elements 
2N— the elements of the array A.
Output Format
For each test case output the answer on a new line — Yes if the given array represents a valid list of prices, and No otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e, Yes, YES, and yEs will all be treated as equivalent.

Constraints
1≤T≤10 
1≤N≤10 
 
The sum of N over all testcases does not exceed 2⋅10 

Sample 1:
Input
Output
4
3
4 8 4 6 7 3
3
4 8 6 8 7 8
2
2 4 5 3
4
8 7 9 8 4 6 2 8
Yes
No
Yes
No
Explanation:
Test case 1: One valid way of assigning prices is as follows:

The first candy can have a price of 4 in city 1, 6 in city 2, and 8 in city 3.
The second candy can have a price of 4 in city 1, 3 in city 2, and 7 in city 3.
Since a valid assignment exists, the answer is "Yes".

Test case 2: No valid set of prices exists that could give this array, since 8 would be repeated somewhere.

Test case 3: One way of splitting the prices is [2,5] and [4,3].

Test case 4: No valid set of prices exists that could give this array.'''

for _ in range(int(input())):
    N=int(input())
    arr=list(map(int,input().split()))
    valid=True
    for i in arr:
        if arr.count(i)>2:
            valid=False
            break
    if valid:
        print("Yes")
    else:
        print("No")