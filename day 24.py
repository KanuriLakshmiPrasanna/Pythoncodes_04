'''Sale Season
It's the sale season again and Chef bought items worth a total of X rupees. The sale season offer is as follows:
if X≤100, no discount.
if 100<X≤1000, discount is 25 rupees.
if 1000<X≤5000, discount is 100 rupees.
if X>5000, discount is 500rupees
Find the final amount Chef needs to pay for his shopping.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of single line of input containing an integer X.
Output Format
For each test case, output on a new line the final amount Chef needs to pay for his shopping.

Input
Output
4
15
70
250
1000
15
70
225
975
Explanation:
Test case 1: Since X≤100, there is no discount.

Test case 3: Here, X=250. Since 100<250≤1000, discount is of 25 rupees. Therefore, Chef needs to pay 250−25=225 rupees.'''

T=int(input())

for _ in range(T):
    X=int(input())
    if X<=100:
        print(X)
    elif 100<X<=1000:
        print(X-25)
    elif 1000<X<=5000:
        print(X-100)
    else:
        print(X-500)