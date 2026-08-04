# Question: Check whether a given string is a palindrome using slicing.
letter = "sir"
if letter == letter[::-1]:
    print("palindrome")
else:
    print('not a palindrome')
