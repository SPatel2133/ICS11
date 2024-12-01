#Harp Tuning
instructions = input("Enter instructions: ")  # Example: "AFB+8HC-4"
letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"


current = ""  # Variable to hold the current segment


for i in range(len(instructions)):
    char = instructions[i]
    
    # Process letters
    if char in letters:
        current += char


    # Process '+' or '-'
    elif char == "+":
        current += " tighten "
    elif char == "-":
        current += " loosen "


    # Process numbers
    elif char in numbers:
        current += char


    # Check if the current segment ends
    if i + 1 >= len(instructions) or instructions[i + 1] in letters:
        print(current)  # Print the completed segment
        current = ""  # Reset for the next segment
