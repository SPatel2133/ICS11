# Creating a Python file with all the formatted output examples combined

code = """
# 1. Basic String Formatting
name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name, age))  # Positional formatting

# 2. f-Strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# 3. String Formatting with .format()
# Positional Arguments
print("{0} is {1} years old.".format("Alice", 25))

# Keyword Arguments
print("{name} is {age} years old.".format(name="Alice", age=25))

# 4. Number Formatting
pi = 3.14159
# Decimal Places
print("{:.2f}".format(pi))  # Output: 3.14

# Padding and Alignment
print("{:<10}".format("left"))    # Left align (10 spaces)
print("{:>10}".format("right"))   # Right align (10 spaces)
print("{:^10}".format("center"))  # Center align (10 spaces)

# Zero Padding
number = 5
print("{:05}".format(number))  # Output: 00005

# 5. Hexadecimal, Binary, and Octal Representation
number = 255
print("Hex: {0:x}, Binary: {0:b}, Octal: {0:o}".format(number))

# 6. Percentage Formatting
percentage = 0.75
print("{:.2%}".format(percentage))  # Output: 75.00%

# 7. Escape Braces in .format()
print("Use {{ and }} to escape braces.".format())

# 8. Formatting Numbers with Commas
large_number = 1000000
print("{:,}".format(large_number))  # Output: 1,000,000
"""
x = 1
print(x)