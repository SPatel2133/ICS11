numRows = 5 # Example input
triangle = []

# Build Pascal's Triangle row by row
for i in range(numRows):
    # Start each row with 1
    row = [1] * (i + 1)
    # Calculate the values in between the 1s for rows beyond the second row
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    # Append the row to the triangle
    triangle.append(row)

print(triangle)

