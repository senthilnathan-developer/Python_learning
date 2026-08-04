# Question: Create a function that counts the words in a sentence.
def count_word(word):
  sentence = word.split()
  print(len(sentence))
      
count_word("I am learn python")
