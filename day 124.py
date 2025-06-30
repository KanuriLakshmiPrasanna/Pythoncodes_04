'''You are given a list of n-1 integers from 1 to n. These numbers are in random order and one number is missing. Write a Python program to find the missing number.
Input: [3, 7, 1, 2, 8, 4, 5]
Output: 6'''

def missing():
    lst=list(map(int,input().split()))
    lst.sort()
    for i in range(1,max(lst)):
        if i>0:
            if i not in lst:
                print(i)
                break
    else:
        print(max(lst)+1)
missing()
