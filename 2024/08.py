# damn cant even get top 1000 recently.
# got stuck on antinodes possibly being between two antennas which apparantly wasn't a thing so it didnt matter
from collections import defaultdict

with open("8.txt", "r") as file:
    lines = [line.strip() for line in file]

ants = defaultdict(list)

for row, line in enumerate(lines):
    for col, v in enumerate(line):
        if v != ".":
            ants[v].append((row, col))

taken = [[False] * len(row) for row in lines]

for ant, positions in ants.items():
    for a in positions:
        for b in positions:
            if a == b:
                taken[a[0]][a[1]] = True
                continue
            d = (a[0] - b[0], a[1] - b[1])  # b to a
            new_pos = (b[0] + 2 * d[0], b[1] + 2 * d[1])
            while 0 <= new_pos[0] < len(lines) and 0 <= new_pos[1] < len(lines[0]):
                taken[new_pos[0]][new_pos[1]] = True
                new_pos = (new_pos[0] + d[0], new_pos[1]+d[1])

t = 0
for r in taken:
    t += sum(r)
print(t)
