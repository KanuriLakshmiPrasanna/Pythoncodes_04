'''Grades of Student
Write a program to print the grades of a student based on the marks he/she has obtained provided as input. The student is graded A if marks are greater than 90, B if marks are greater than 70, C if greater than or equal to 40, else F.

Sample 1:
Input
Output
95
A   
Sample 2:
Input
Output
40
C
Sample 3:
Input
Output
20
F'''
marks=int(input())
if marks>90:
    print('A')
elif marks >70:
    print('B')
elif marks>=40:
    print('C')
else:
    print('F')