with open("3.txt", "r") as f:
    pairs = [[]]
    for l in f:
        line = l.strip()
        if len(pairs[-1]) == 3:
            pairs.append([])
        pairs[-1].append(line)


weights = "abcdefghijklmnopqrstuvwxyz"
weights = weights + weights.upper()
total = 0
for a, b, c in pairs:
    for char in a:
        if char in b and char in c:
            total += weights.index(char) + 1
            break
print(total)