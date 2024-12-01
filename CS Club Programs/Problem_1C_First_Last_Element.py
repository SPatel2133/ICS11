nums = [5, 7, 7, 8, 8, 10]
target = 8
#Initialize Start and End at -1 since target hasn't been found initially
start = -1
end = -1

for i in range(len(nums)):
    if nums[i] == target:
        if start == -1:
            start = i  # Set the first occurrence
        end = i  # Update the last occurrence continuously
if (start or end) == -1:
    print([-1,-1])
else:
    print([start,end])
    
