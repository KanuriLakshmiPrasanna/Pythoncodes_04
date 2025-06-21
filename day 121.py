'''print the letter and number of times it appears in the string
Example: aaabbc output: a3b2c1'''
S=input()
lst=[]
for i in S:
    if i not in lst:
        lst.append(i)
        if i in lst:
            print(i,S.count(i),sep='',end=' ')
