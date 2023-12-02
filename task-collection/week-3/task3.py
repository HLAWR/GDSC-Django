word=input("Enter the word: ")
rword=word[::-1]
if word==rword:
    print("The word ", word, " is a palindrome.")
else:
    print("The word ", word, " is not a palindrome.")
