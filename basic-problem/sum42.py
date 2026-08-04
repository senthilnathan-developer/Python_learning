# Question: Print the first 10 numbers of the Fibonacci sequence.
number = 10

a = 0
b = 1
for i in range(number):
    print(a)
    c = a+b
    a=b
    b=c
