start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Iterate through each number in the range
for number in range(start_range, end_range + 1):
    divisor = number - 1
    # Check if the number is prime
    while divisor >= 2:
        if number % divisor == 0:
            break
        divisor -= 1
    else:
        if number > 1:  # Prime numbers are greater than 1
            print(number)
