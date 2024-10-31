#BMI calc
weight = eval(input())
height = eval(input())
bmi = (weight / (height * height))
if  bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 25:
    print("Normal weight")
elif 25 < bmi:
    print("Overweight")
