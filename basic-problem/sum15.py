# Question: Create a function that checks whether a word is a palindrome.
def pallindrome(word):
    reverse = word[::-1]
    
    if  word == reverse:
            print("pallindrome")
    else:
            print("not a pallindrome")
            
pallindrome("sir")
