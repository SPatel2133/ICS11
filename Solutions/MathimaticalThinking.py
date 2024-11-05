# This program checks if the result of various mathematical operations 
# between two numbers (a and b) equals a third number (c).

# Input: Get three numbers from the user
a = int(input("Give Number a: "))
b = int(input("Give Number b: ")) 
c = int(input("Give Number c: "))  

#Computation:
# Check if the sum of a and b equals c
if a + b == c:
    print("Possible") 

# Check if the difference of a and b equals c
elif a - b == c:
    print("Possible") 

# Check if the product of a and b equals c
elif a * b == c:
    print("Possible")  

# Check if the integer division of a by b equals c
elif a // b == c:
    print("Possible") 

# Output: If none of the conditions are met, print "Impossible"
else:
    print("Impossible") 
