# Didn't read part A correctly, thought it was just looking for the min distance with a cheat so took some time.
# Other than that really fun day.
with open("20.txt", "r") as file:
    grid = [line.strip() for line in file]

seen = [[False]*len(line) for line in grid]

start, end = (-1, -1), (-1, -1)
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "S":
            start = (r, c)
        if val == "E":
            end = (r, c)


def neighbours(row, col):
    out = []
    for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nr, nc = row + d[0], col + d[1]
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            out.append((nr, nc))
    return out


pos = start
prev = start
d_to_end = [[-1]*len(line) for line in grid]
path = []
while pos != end:
    for npos in neighbours(*pos):
        if grid[npos[0]][npos[1]] != "#" and npos != prev:
            path.append(pos)
            prev, pos = pos, npos
            break
path.append(end)

for i, p in enumerate(path):
    d_to_end[p[0]][p[1]] = len(path)-i-1

paths = set(path)
total = 0

for pos in path:
    for r in range(max(0, pos[0]-20), min(len(grid), pos[0]+21)):
        for c in range(max(0, pos[1]-20), min(len(grid[0]), pos[1]+21)):
            d = abs(r-pos[0])+abs(c-pos[1])
            if d > 20:
                continue
            if (r, c) in paths and (saved := d_to_end[pos[0]][pos[1]] - d_to_end[r][c] - d) >= 100:
                total += 1
print(total)
