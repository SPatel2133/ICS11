# Creating a Python file for conditional control examples

conditional_code = """
# 1. Simple if statement
x = 10
if x > 5:
    print("x is greater than 5")

# 2. if-else statement
y = 4
if y > 5:
    print("y is greater than 5")
else:
    print("y is 5 or less")

# 3. if-elif-else ladder
z = 8
if z > 10:
    print("z is greater than 10")
elif z == 8:
    print("z is exactly 8")
else:
    print("z is less than 8")

# 4. Nested if statements
a = 15
if a > 10:
    if a < 20:
        print("a is between 10 and 20")

# 5. Ternary operator (conditional expression)
b = 5
result = "Greater than 3" if b > 3 else "3 or less"
print(result)

# 6. Using logical operators
c = 7
if c > 5 and c < 10:
    print("c is between 5 and 10")

# 7. Using 'in' for membership tests
char = 'x'
if char in "xyz":
    print(f"{char} is in the string")

# 8. Using 'is' for identity comparison
list1 = [1, 2, 3]
list2 = list1
if list1 is list2:
    print("list1 and list2 are the same object")

# 9. Checking for None
value = None
if value is None:
    print("value is None")
"""
x = 1
print(x)