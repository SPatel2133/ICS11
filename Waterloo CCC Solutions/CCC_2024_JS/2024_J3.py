#Bronze Count WORK!
temp = []
bronze_amount = 0
while True:
    total = int(input())
    break

for i in range (total):
    scores = eval(input())
    temp.append(scores)
    
final = sorted(set(temp))
bronze = final[-3]
bronze_amount = temp.count(bronze)
print(bronze,bronze_amount)