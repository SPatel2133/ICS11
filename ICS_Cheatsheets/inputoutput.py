# Creating a Python file for input and output examples

input_output_code = """
# 1. Basic input from the user
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 2. Input with type conversion (int)
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# 3. Reading multiple inputs (space-separated)
x, y = input("Enter two numbers separated by space: ").split()
print(f"First number: {x}, Second number: {y}")

# 4. Input with a custom prompt and handling floats
height = float(input("Enter your height in meters: "))
print(f"Your height is {height:.2f} meters.")

# 5. File Output - Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write(f"User name: {name}\n")
    file.write(f"User age: {age}\n")

# 6. File Input - Reading from a file
with open("output.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# 7. Print formatting options
pi = 3.14159
print("The value of pi is {:.2f}".format(pi))  # Using format
print(f"The value of pi is {pi:.2f}")  # Using f-string

# 8. Printing multiple values with separators
print("apple", "banana", "cherry", sep=", ")

# 9. Printing with end parameter
print("This is", end=" ")
print("on the same line.")
"""
x = 1
print(x)
