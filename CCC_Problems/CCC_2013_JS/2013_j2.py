#ROtating LETTERS
letters = ["I","O","S","H","Z","X","N"]
word = input()
no = 0
yes = 0
for i in word:
    if i not in letters:
        no += 1
    else:
        yes += 1
if no > 0:
    print("NO")
else:
    print("YES")