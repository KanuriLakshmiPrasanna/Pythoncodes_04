#QUESTION 1
'''write a program that reads 3 numbers as parameters print the maximum number without using max() built-in function.'''
def max_num(a,b,c):
        if a>=b and a>=c:
                return a
        elif b>=a and b>=c:
                return b
        elif c>=a and c>=b:
                return(c)


a,b,c=map(int,input().split())
maximum=max_num(a,b,c)
print(maximum)
