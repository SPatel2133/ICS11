#winning score
appletotal = 0
bananatotal = 0
appletotal += int(input())*3
appletotal += int(input())*2
appletotal += int(input())
bananatotal += int(input())*3
bananatotal += int(input())*2
bananatotal += int(input())
    
if appletotal == bananatotal:
    print("T")
elif appletotal > bananatotal:
    print("A")
else:
    print("B")


