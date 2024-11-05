#Nikki and Byron
#INCOMPLETE NEEDS FUNCTIONS TO SOLVE

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
byron = 0
nikki = 0
for i in range (1,s+1):
    nikki += a-b
    byron += c-d
    if nikki > byron:
        print(i)

