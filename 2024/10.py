# I kid you not i read part A wrong and accidentally solved B. Then solved A, read B and spammed ctrl-Z
with open("10.txt", "r") as file:
    grid = [list(map(int, line.strip())) for line in file]


def get_neighbours(r, c):
    out = []
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr = r + d[0]
        nc = c + d[1]
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            out.append((nr, nc))
    return out


def score(r, c):
    val = grid[r][c]
    if val == 9:
        return 1
    out = 0
    for n in get_neighbours(r, c):
        if grid[n[0]][n[1]] == val + 1:
            out += score(*n)
    return out


t = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 0:
            s = score(r, c)
            t += s
print(t)
