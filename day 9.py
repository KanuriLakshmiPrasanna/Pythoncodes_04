'''Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ...
 and space after each, and then the word is pronounced with a question mark ?.

Examples
stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"'''

def stutter(word):
    print(f"{word[:2]}...{word[:2]}...{word}?")

word=input("Enter a word:")
stutter(word)