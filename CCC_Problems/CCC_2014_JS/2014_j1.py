#triangle times

a = int(input())
b = int(input())
c = int(input())

if a == b == c: 
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isoceles")
elif a != b != c:
    print("Scalene")
else:
    print("Error")