'''Chef wants to count the number of vowels in the given word.Help him to find it.
NOTE: Vowels include a,e,i,o,u in both upper and lower case'''

s = "beautiful day"
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print("Number of vowels:", count)
