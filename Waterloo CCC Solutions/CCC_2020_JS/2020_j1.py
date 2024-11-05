#Dog Treats

small_treats = int(input())
medium_treats = int(input())
large_treats = int(input())

happiness = 1*small_treats + 2*medium_treats + 3*large_treats

print(happiness)

if happiness >= 10:
    print("happy")
else:
    print("sad")