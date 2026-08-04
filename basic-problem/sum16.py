# Question: Create a function that counts the consonants in a string.
def count_consonent(word):
    count =0
    consonent = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    for char in word:
        if char in consonent:
            count+=1
    print(count)
count_consonent('python')

