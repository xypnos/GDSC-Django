word = input("Enter a word: ")

if word.lower() == word.lower()[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
