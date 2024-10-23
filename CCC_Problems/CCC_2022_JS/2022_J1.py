#Cupcake Party
reg_box = int(input())*8
small_box = int(input())*3

leftover = ((reg_box+small_box)%28)
print(leftover)