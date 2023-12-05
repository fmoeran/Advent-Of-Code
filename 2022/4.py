with open("4.txt", "r") as f:
    data = []
    for l in f:
        line = l.strip()
        data.append(line.split(","))

total = 0
for a, b in data:
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    if (b1<=a2<=b2) or (b1<=a1<=b2) or a1<=b1<=a2 or a1<=b2<=a2:
        total += 1
print(total)


