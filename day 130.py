''' Write a program that reads a string and prints the character of your string in reverse order. 
Sample input1: 
Scale 
Sample output1: 
e 
l 
a 
c 
S 
Sample input2: 
Metrics 
Sample output2: 
s 
c 
i 
r 
t 
e 
M'''

S = input("Enter a string: ")
word=input()
lst=list(word)
for i in range(len(word)):
    print(lst.pop())


#(or)
word=input()
for i in range(len(word)-1,-1,-1):# in braces we used string slicing len(word)-1 is start=4 and -1 is end, so it goes until 0 index and next is step=-1 to go in reverse order
    print(word[i])
#(or)   