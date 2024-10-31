#Vote Count
votes = int(input())
vote = input()
A = int(vote.count("A"))
B = int(vote.count("B"))

if A == B:
    print("Tie")
elif A > B:
    print("A")
else:
    print("B")