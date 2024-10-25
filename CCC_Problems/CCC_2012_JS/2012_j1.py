#Speed limits are not fine!
limit = int(input())
speed = int(input())

check = speed - limit
print(check)

if 31 <= check:
    print("You are speeding and your fine is $500.")
elif 21 <= check:
    print ("You are speeding and your fine is $270.")
elif 1 <= check:
    print ("You are speeding and your fine is $100.")
else:
    print("Congratulations, you are within the speed limit!")