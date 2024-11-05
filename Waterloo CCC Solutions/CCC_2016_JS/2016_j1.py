#Tournament selections
wins = 0
for i in range (6):
    games = (input()).upper()
    if games == "W":
        wins += 1
if (wins == 5) or (wins == 6):
    print("1")
elif (wins == 4) or (wins == 3):
    print('2')
elif (wins == 2) or (wins == 1):
    print('3')
else:
    print('-1')