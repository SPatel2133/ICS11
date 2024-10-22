#Bronze Count WORK!
temp = []

while True:
    total = int(input())
    break

for i in range (total):
    scores = eval(input())
    temp.append(scores)
    
final = sorted(set(temp))
print(final[-3], temp.count(final[-3]))