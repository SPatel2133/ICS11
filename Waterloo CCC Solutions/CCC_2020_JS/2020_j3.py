#Art
x = []
y = []
drops = int(input())
for i in range(drops):
    x1, y1 = map(int, input().split(","))
    x.append(x1)
    y.append(y1)
    
ymax = max(y) + 1
ymin = min(y) - 1
xmax = max(x) + 1
xmin = min(x) - 1

print(xmin,ymin,sep=",")
print(xmax,ymax,sep=",")
