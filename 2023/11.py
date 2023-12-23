# Easiest part 2 I've ever done?
# just change lines 14 and 19 from 2 to 1000000
with open("11.txt", "r") as f:

    arr = [line.strip() for line in f]

expansion = 1000000

row_weights = [1]*len(arr)
col_weights = [1]*len(arr[0])
gals = []
n = 0
for r, row in enumerate(arr):
    n += row.count("#")
    if "#" not in row:
        row_weights[r] = expansion
for c in range(len(arr)):
    col = [row[c] for row in arr]
    n += col.count("#")
    if "#" not in col:
        col_weights[c] = expansion




for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == "#":
            gals.append((r, c))



total = 0
for i in range(len(gals)):
    for j in range(i+1, len(gals)):
        dist = 0
        rstart, rend = min(gals[i][0]+1, gals[j][0]+1), max(gals[i][0], gals[j][0])
        for r in range(rstart, rend):
            dist += row_weights[r]
        cstart, cend = min(gals[i][1] + 1, gals[j][1] + 1), max(gals[i][1], gals[j][1])
        for c in range(cstart, cend):
            dist += col_weights[c]
        if rstart <= rend:
            dist += 1
        if cstart <= cend:
            dist += 1

        total += dist
print(total)

