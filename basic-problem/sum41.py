numbers = [1, 2, 3, 4, 2, 5, 1, 6,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

# duplicate = []

# for i in numbers:
#     if numbers.count(i) > 1 and i not in duplicate:
#         duplicate.append(i)

# print(duplicate)


duplicate = []

for i in numbers:
    if numbers.count(i) > 1:
        duplicate.append(i)

print(duplicate)
