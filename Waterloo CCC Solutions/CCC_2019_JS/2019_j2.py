#Time to decrompress
to_print = []
lines = int(input())#number of lines
for i in range(lines):
    encoded = input().split()
    count = int(encoded[0])
    letter = encoded[1]
    to_print.append(letter * count)
for i in to_print:
    print(i)