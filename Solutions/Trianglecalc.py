
# This program determines the type of triangle based on the sizes of its angles.

# Input section: Get the sizes of all three angles from the user in degrees
angle1 = int(input("First Angle: "))
print()
angle2 = int(input("Second Angle: "))
print()
angle3 = int(input("Third Angle: "))
print()

#Computation + Output Section:
# Check if the total of the angles is 180 degrees
if angle1 + angle2 + angle3 != 180:
    print("Error. No Triangle") 

# Check if all angles are equal if true it's equilateral
elif angle1 == angle2 == angle3: 
    print("Equilateral")  

# Check if exactly two angles are if true it's isosceles
elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
    print("Isosceles")  

# If no angles are the same, it must be a scalene triangle
else:
    print("Scalene")
