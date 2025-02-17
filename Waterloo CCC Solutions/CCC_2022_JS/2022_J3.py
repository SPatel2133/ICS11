
instructions = input("Enter Instructions ")
current = ""


for i in range(len(instructions)):
   if instructions[i].isalpha():
       current += instructions[i]
   elif instructions[i] == "+":
       current += " tighten "
   elif instructions[i] == "-":
       current += " loosen "
   elif instructions[i].isdigit():
       current += instructions[i]
       print(current)
       current = ""