'''
    Write a program to check if a string is a palindrome.
'''

def isPalindrome(string):
    reverse_String=string[::-1]
    return string == reverse_String


word=input("enter a string")
if isPalindrome(word):
    print(f"{word} is palindrome.")
else:
    print(f"{word} is not a palindrome.")