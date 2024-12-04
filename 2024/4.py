# DAMN I TOOK FOREVER ON PART A. leave it to me to forget a cardinal direction exists lmao.
# That's such a basic question too!
# pretty quick B tho.

from re import findall

with open("4.txt", "r") as file:
    lines = [line.strip() for line in file]

n = len(lines)
rows = [[c for c in line] for line in lines]
cols = [[row[col] for row in lines] for col in range(n)]
dup = [[lines[j][i + j] for j in range(n - i)] for i in range(n)]
ddown = [[lines[i + j + 1][j] for j in range(n - i - 1)] for i in range(n)]
uup = [[lines[n - 1 - j][i + j] for j in range(n - i)] for i in range(n)]
udown = [[lines[n - 1 - (i + j + 1)][j] for j in range(n - i - 1)] for i in range(n)]

t = 0
for ls in [rows, cols, dup, ddown, uup, udown]:
    for s in ls:
        t += len(findall(r"XMAS", "".join(s)))
        t += len(findall(r"SAMX", "".join(s)))
# print(t)


#part 2

t = 0
for row in range(1, n - 1):
    for col in range(1, n - 1):
        if lines[row][col] != "A":
            continue
        a = lines[row - 1][col - 1] + lines[row][col] + lines[row + 1][col + 1]
        b = lines[row - 1][col + 1] + lines[row][col] + lines[row + 1][col - 1]
        if (a == "MAS" or a == "SAM") and (b == "MAS" or b == "SAM"):
            t += 1
print(t)
