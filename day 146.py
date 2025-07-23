'''Check if a given word contains all the vowels or not
if it contains all the vowels print True else false
'''

word = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u']

if all(v in word for v in vowels):
    print("true")
else:
    print("false")
