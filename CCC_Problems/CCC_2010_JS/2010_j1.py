#What is n

n = int(input())

if n % 5 == 2 or n % 5 == 3: print(2)
else:
    if n <= 5: 
        if n == 1: print(1)
        elif n >= 4: print(3)
    elif n > 5:
        if n % 5 == 1: print(3)
        elif n % 5 >= 4 or n % 5 == 0: print(1) 