#Special Day
month = int(input())
day = int(input())

if 2 > month:
    print("Before")
elif month == 2:
    if 18 > day:
        print("Before")
    elif day == 18:
        print("Special")
    elif 18 < day:
        print("After")
else:
    print("After")
