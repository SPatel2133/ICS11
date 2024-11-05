copies = float(input("Enter the Number of copies you wish to print: "))
if copies > 1000:
    totalcopies = round(copies*.25,2)
elif copies >= 750:
    totalcopies = round(copies*.26,2)
elif copies >= 500:
    totalcopies = round(copies*.27,2)
elif copies >= 100:
    totalcopies = round(copies*.28,2)
else:
    totalcopies = round(copies*.3,2)

print("price per copy is:", totalcopies/copies)
print("Total cost for the copies is: ",totalcopies)
   
