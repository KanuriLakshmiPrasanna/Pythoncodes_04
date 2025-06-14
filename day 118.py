
#calculate sum of +ve and -ve integers, once user enter '0' exit from loop
number=int(input("Enter number(0 to exit):"))
sum=0
while number!=0:
    sum+=number
    number=int(input("Enter number(0 to exit):"))
print("Total sum is:",sum)
