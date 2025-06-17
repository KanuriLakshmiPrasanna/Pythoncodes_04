'''Positive and Negative
Write a program to check whether a number given as user input is positive, negative, or zero.

Sample 1:
Input
Output
20
Positive
Sample 2:
Input
Output
0
Zero
Sample 3:
Input
Output
-95
Negative'''

num=int(input())
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")