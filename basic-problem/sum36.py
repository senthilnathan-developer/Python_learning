a = int(input())
b = int(input())
c = int(input())

if a >= b and b >= a:
    print(a)
elif b >= c and c >= b:
    print(b)
else:
    print(c)
