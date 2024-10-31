spaces = int(input())
yesterday = input()
today = input()
a = 0
for i in range(spaces):
    if (yesterday[i] == "C") and (today[i] == "C"):
        a += 1
print(a)
    
    