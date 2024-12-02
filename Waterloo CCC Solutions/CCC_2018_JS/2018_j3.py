#Are we there yet? brute force problem

# Input: distances between consecutive cities
b, c, d, e = input().split()
city2, city3, city4, city5 = int(b), int(c), int(d), int(e)

# Precompute cumulative distances from city 1 to each city
dist1_to_2 = city2
dist1_to_3 = city2 + city3
dist1_to_4 = city2 + city3 + city4
dist1_to_5 = city2 + city3 + city4 + city5

# Store the cumulative distances for easy lookup
distances = [
    [0, dist1_to_2, dist1_to_3, dist1_to_4, dist1_to_5],
    [dist1_to_2, 0, city3, city3 + city4, city3 + city4 + city5],
    [dist1_to_3, city3, 0, city4, city4 + city5],
    [dist1_to_4, city3 + city4, city4, 0, city5],
    [dist1_to_5, city3 + city4 + city5, city4 + city5, city5, 0]
]

# Output the distance table by simply printing the precomputed distances
for row in distances:
    print(" ".join(map(str, row)))
