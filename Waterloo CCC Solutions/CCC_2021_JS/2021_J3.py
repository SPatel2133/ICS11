#Secret Instructions
temp = ""
direction = ""
while True:
    temp = input()
    if temp == "99999":
        break
    
    sum_of = int(temp[0]) + int(temp[1])
    steps = temp[2:]
    
    if sum_of == 0:
        print(direction, steps)
        
    elif sum_of % 2 == 1:
        direction = "left"
        print("left", steps)
    
    else:
        direction = "right"
        print("right", steps)


        
        
    