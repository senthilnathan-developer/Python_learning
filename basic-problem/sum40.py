# Question: Check whether a string is a palindrome without using slicing.
letter = "sir"
rev = ""
for i in letter:
    rev = i + rev

if rev == letter:
        print(letter,"is Pallindrome")
else:
        print(letter ,"not a Pallindrome")
   
