#Chilli Peppers
scoville = 0
peppers = int(input())
for i in range(peppers):
    inpute = input().lower()
    if inpute == "poblano":
        scoville += 1500
    elif inpute == "mirasol":
        scoville += 6000
    elif inpute == "serrano":
        scoville += 15500
    elif inpute == "cayenne":
        scoville += 40000
    elif inpute == "thai":
        scoville += 75000
    elif inpute == "habanero":
        scoville += 125000
print(scoville)
