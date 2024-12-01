# Cold Compress

iterations = int(input())

for _ in range(iterations):
    encoded = input()
    count = 1  # Start counting the first character

    for i in range(1, len(encoded)):  # Start from the second character
        if encoded[i] == encoded[i - 1]:
            count += 1  # Increment count for consecutive characters
        else:
            print(count, encoded[i - 1], end=" ")  # Print count and character
            count = 1  # Reset count for the new character
    
    # Print the last group after the loop
    print(count, encoded[-1])
