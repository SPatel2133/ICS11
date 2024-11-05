#Problem J1: Deliv-e-droid
package = int(input(""))
collisions = int(input(""))
total_package = package*50
total_collision = collisions*10        
total = (total_package - total_collision) 
if package>collisions:
    print(total + 500)
else:
    print(total)
