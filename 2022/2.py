with open("2.txt", "r") as f:
    data = []
    for l in f:
        line = l.strip()
        data.append(l.split())

vals = "ABC"
score = 0
for a, b in data:
    if b == "Y":
        score += vals.index(a)+1
        score += 3
    elif b == "Z":
        score += (vals.index(a)+1)%3+1
        score += 6
    else:
        score += (vals.index(a)-1)%3+1


print(score)
