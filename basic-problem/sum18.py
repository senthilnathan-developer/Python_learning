# Question: Create a function that calculates the sum of the digits in a number.
def sum_number(number):
   sum = 0
   for num in str(number):
      sum+=int(num)
   print(sum)

      
sum_number(12345)

