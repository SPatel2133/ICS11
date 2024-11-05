weight = int(input("Enter package weight in kilograms:")) 
l = int(input("Enter package length in centimeters: "))
w = int(input("Enter package width in centimeters: "))
h = int(input("Enter package height in centimeters: ")) 

size = l*w*h

if weight > 27 and size > 100000:
    print("To Heavy and To Large")
elif weight>27:
    print("To Heavy!")
elif size>100000:
    print("To Large!")
else: 
    print("OK!")