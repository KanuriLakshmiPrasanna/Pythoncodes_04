'''Palindrome of a given number. Check if the given number is Palindrome or not'''

num = int(input("Enter a number: "))
temp = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
