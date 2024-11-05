#Special Event
days = int(input())
freqancy = [0]*5
for i in range(days):
    available_days = input().lower()
    for i in range(5):
        if available_days[i]== 'y':
            freqancy[i]+=1

result = []
best_day = max(freqancy)
for i in range(5):
    if freqancy[i] == best_day:
        result.append(i+1)
print(*result,sep=',')