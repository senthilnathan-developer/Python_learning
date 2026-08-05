#Problem: Check whether a given number is an Armstrong number.

number = int(input("Enter a number: "))

total = 0

for digit in str(number):
    total += int(digit) ** len(str(number))

if total == number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")