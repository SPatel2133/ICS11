# Creating a Python file for print statement examples

print_code = """
# 1. Basic print statement
print("Hello, World!")

# 2. Print multiple items
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# 3. Print with custom separator
print("Apple", "Banana", "Cherry", sep=", ")

# 4. Print without newline
print("Hello", end=" ")
print("World!")

# 5. Print formatted strings using f-strings (Python 3.6+)
pi = 3.14159
print(f"Value of pi: {pi:.2f}")

# 6. Print formatted strings using .format()
print("Name: {}, Age: {}".format(name, age))

# 7. Print with zero padding and alignment
number = 5
print("{:05}".format(number))  # Output: 00005
print("{:<10}".format("left"))  # Left aligned
print("{:>10}".format("right"))  # Right aligned

# 8. Print with file redirection
with open("print_output.txt", "w") as file:
    print("This is redirected output.", file=file)

# 9. Printing with comma-separated values
x = 10
y = 20
print("Sum of", x, "and", y, "is", x + y)
"""
x = 1
print(x)