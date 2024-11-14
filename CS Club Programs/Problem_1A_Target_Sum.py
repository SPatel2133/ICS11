from random import *
numbers = [] #Initialize list for all number
arraysize = int(input("Size of the array ")) #Get user input for arraysize

#append all numbers into the numbers list
for i in range(arraysize):
    numbers.append(randint(2,199))
print(numbers)
#Prompt user for a target number 
target = int(input("Target Number "))

found = False
for i in range(len(numbers)):
    for j in range(i+1,arraysize):
        if numbers[i] + numbers[j] == target:
            print(i,j)
            found = True
            break
        if found:
            break
if not found:
    print("No Solutions")
