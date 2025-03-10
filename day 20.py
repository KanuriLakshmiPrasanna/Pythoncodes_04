'''Mahasena
Kattapa, as you all know was one of the greatest warriors of his time. The kingdom of Maahishmati had never lost a battle under him (as army-chief), and the reason for that was their really powerful army, also called as Mahasena.

Kattapa was known to be a very superstitious person. He believed that a soldier is "lucky" if the soldier is holding an even number of weapons, and "unlucky" otherwise. He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" soldiers, and "NOT READY" otherwise.

Given the number of weapons each soldier is holding, your task is to determine whether the army formed by all these soldiers is "READY FOR BATTLE" or "NOT READY".'''



'''Sample 1:
Input
Output
1
1
NOT READY
Explanation:
Example 1: For the first example, N = 1 and the array A = [1]. There is only 1 soldier and he is holding 1 weapon, which is odd. The number of soldiers holding an even number of weapons = 0, and number of soldiers holding an odd number of weapons = 1. Hence, the answer is "NOT READY" since the number of soldiers holding an even number of weapons is not greater than the number of soldiers holding an odd number of weapons.
Sample 2:
Input
Output
1
2
READY FOR BATTLE
Explanation:
Example 2: For the second example, N = 1 and the array A = [2]. There is only 1 soldier and he is holding 2 weapons, which is even. The number of soldiers holding an even number of weapons = 1, and number of soldiers holding an odd number of weapons = 0. Hence, the answer is "READY FOR BATTLE" since the number of soldiers holding an even number of weapons is greater than the number of soldiers holding an odd number of weapons.'''

# cook your dish here
N=int(input())
Arr=list(map(int,input().split()))
count_even,count_odd=0,0
for num in Arr:
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1
if count_even>count_odd:
    print('READY FOR BATTLE')
else:
    print('NOT READY')