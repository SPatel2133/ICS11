
# This program calculates the total calories of a meal at Chips Fast Food.
# User inputs their choices for each part of the meal, and the program sums up the total calories.

# Displaying a welcome message
print("Welcome to Chip's Fast Food Emporium")
print()

# Input section: Prompt user for their menu choices
burger = int(input("Please enter a burger choice: "))
print()
sides = int(input("Please enter a side order choice: "))
print()
drink = int(input("Please enter a drink choice: "))
print()
dessert = int(input("Please enter a dessert choice: "))
print()

#Computation:
# Initialize a variable to keep track of total calories for the meal
total_calories = 0  

# Burger choice: Add corresponding calories to total based on user choice
if burger == 1:
    total_calories += 461  #Cheeseburger
elif burger == 2:
    total_calories += 431  #Fish Burger
elif burger == 3:
    total_calories += 420  #Veggie Burger

#No else statement since input 4 would add 0 calories to the total

# Side choice: Add corresponding calories to total 
if sides == 1:
    total_calories += 100  #Fries
elif sides == 2:
    total_calories += 57   #Baked Potato
elif sides == 3:
    total_calories += 70   #Chef Salad


# Drink choice: Add corresponding calories to total 
if drink == 1:
    total_calories += 130  #Soft Drink
elif drink == 2:
    total_calories += 160  #Orange Juice
elif drink == 3:
    total_calories += 118  #Milk


# Dessert choice: Add corresponding calories to total 
if dessert == 1:
    total_calories += 167  #Apple Pie
elif dessert == 2:
    total_calories += 266  #Sundae
elif dessert == 3:
    total_calories += 75   #Fruit Cup


#Output: the total calorie count for the meal
print("Your total calories count for this meal is {}.".format(total_calories))
