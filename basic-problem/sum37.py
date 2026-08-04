# Question: Reverse a string without using slicing.
# str = "senthil"

# print(str[::-1])


str = "senthilnathan"
r = ""

for i in str:
  r = i + r

print(r)
