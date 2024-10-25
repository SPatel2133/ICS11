#shifty sums
initial = int(input())
shifty = int(input())
final= 0
for i in range(shifty+1):
    final += initial*(10**i)
print(final)