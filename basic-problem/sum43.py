number = [12,34,56,78]
largest = number[0]
second_largest = number[0]

for i in number:
    if i > largest:
        largest = i



for i in number:
    if i > second_largest and i != largest:
        second_largest = i

print(second_largest)


