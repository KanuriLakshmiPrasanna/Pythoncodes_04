#To check Curzon number or not
#CURSON NUMBER- if 2**num+1 is dividible by 2*num+1 it is called as curzon number
def is_curzon(num):
    exponent=2**num+1
    multiple=2*num+1
    if exponent%multiple==0:
        print(f"{num} is curzon")
    else:
        print(f"{num} is not curzon")
    
    
number=int(input("Enter a number to check it is curzon or not: "))
is_curzon(number)