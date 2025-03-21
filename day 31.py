#Finding no.of vowels and Consonants in given word
word=input("Enter a word:")
count=0
count1=0
vowels=['A','E','I','O','U','a','e','i','o','u']
for letter in word:
  if letter in vowels:
    count+=1
  else:
    count1+=1
print(f"No. of vowels in {word}:{count}")
print(f"No. of Consonants in {word}:{count1}")
