#Dusa and the Yobis

dusa_size = int(input(""))
dusa = dusa_size
while True:
    yobi = int(input())
    if yobi >= dusa:
        print(dusa)
        break
    dusa += yobi
