#CCC Epidemiology
P = int(input())
N = int(input())
R = int(input())
totalinfections = 0
days = 0
active = N


while P >= N:
    active = active*R
    N += active
    days += 1
    
print(days)        