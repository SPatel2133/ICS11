#Boiling Water
b = int(input())

p = 5*b - 400
if p > 100:
    print(p)
    print(-1)
elif p == 100:
    print(p)
    print(0)
else:
    print(p)
    print(1)

