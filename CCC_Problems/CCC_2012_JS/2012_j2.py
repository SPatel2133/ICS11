#SOUnds Fishy
one = int(input())
two = int(input())
three = int(input())
four = int(input())

if (one - two == 0) and (two-three==0) and (three-four==0):
    print("Fish At Constant Depth")
elif (one - two > 0) and (two - three > 0) and (three - four > 0):
    print("Fish Diving")
elif (one - two < 0) and (two - three < 0) and (three - four < 0):
    print("Fish Rising") 
else:
    print("No Fish")