#Happy or Sad
string = input()
h = int(string.count(":-)"))
s = int(string.count(":-("))
if h == 0 and s == 0:
    print("none")
elif h > s:
    print("happy")
elif s > h:
    print("sad")
elif h == s:
    print("unsure")