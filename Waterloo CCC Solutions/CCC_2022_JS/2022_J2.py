#Ferguson Ball Ratings
players = int(input())
ratings = []
for i in range (players):
    points = int(input())*5
    fouls = int(input())*3
    score = points - fouls
    ratings.append(score)

gold = []
for _ in ratings:
    if _ > 40:
        gold.append(_)
if len(gold) == len(ratings):
    print(len(gold),"+",sep='')
else:
    print(len(gold))