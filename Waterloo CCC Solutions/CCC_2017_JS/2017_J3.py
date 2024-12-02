#Exactly Electical
a, b = input().split()
c, d = input().split()
charge = int(input())

starting_street = int(a)
starting_ave = int(b)

ending_street = int(c)
ending_ave = int(d)

# Calculate the Manhattan distance between the starting and ending points
distance = abs(starting_street - ending_street) + abs(starting_ave - ending_ave)

# Check if we can use exactly the available charge units
if charge >= distance and (charge - distance) % 2 == 0:
    print("Y")
else:
    print("N")
