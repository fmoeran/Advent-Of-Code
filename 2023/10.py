#This one was fun
# Crazy long tho, took me an hour and I still got top 1000 for p2

import sys

sys.setrecursionlimit(1000000)

with open("10.txt", "r") as f:

    grid = [list(line.strip()) for line in f]

incs = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
    ".": [],
    "S": [(-1, 0), (1, 0), (0, -1), (0, 1)]



}

def get_neighbours(row, col):
    return incs[grid[row][col]]


dists = [[float("inf")]*len(grid[0]) for _ in range(len(grid))]
best = 0
def search1(row, col, dist=0):
    dists[row][col] = dist
    char = grid[row][col]
    neighbours = get_neighbours(row, col)
    dists[row][col] = dist
    for r, c in neighbours:
        nr, nc = row+r, col+c
        if nr<0 or nr >= len(grid) or nc<0 or nc >= len(grid[0]):
            continue
        elif dists[nr][nc] <= dist:
            continue

        for rinc, cinc in get_neighbours(nr, nc):
            if (nr+rinc, nc+cinc) == (row, col):
                break
        else:
            continue

        out = search1(nr, nc, dist+1)

start = (0, 0)
for r, row in enumerate(grid):
    if "S" in row:
        start = (r, row.index("S"))
        break
search1(*start)

mx = 0
for r, row in enumerate(dists):
    for c, col in enumerate(row):
        if col == float("inf"):
            grid[r][c] = "."
            continue
        mx = max(mx, col)
        pass


d = {
    (-1, 0): (0, -1),
    (1, 0): (0, 1),
    (0, -1): (1, 0),
    (0, 1): (-1, 0)

}

teams = [[-1 for j in grid[0]] for _ in range(len(grid))]
def get_team(row, col, t):
    global teams

    if teams[row][col] != -1:
        return
    teams[row][col] = t
    #print(teams[row][col])
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row+dr, col+dc
        if nr<0 or nr >= len(grid) or nc<0 or nc >= len(grid[0]):
            continue
        if grid[nr][nc] != ".":
            continue
        get_team(nr, nc, t)

def update_team(nrow, ncol, prow, pcol):
    dif = (nrow - prow, ncol - pcol)
    dincs = d[dif]
    for t, m in enumerate([1, -1]):
        dr, dc = nrow + m * dincs[0], ncol + m * dincs[1]
        if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[0]):
            continue
        if grid[dr][dc] == ".":
            get_team(dr, dc, t)

    for t, m in enumerate([1, -1]):
        dr, dc = prow + m * dincs[0], pcol + m * dincs[1]
        if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[0]):
            continue
        if grid[dr][dc] == ".":
            get_team(dr, dc, t)


num_open = 0
seen = set()
def search2(row, col, prev=(-1, -1)):
    neighbours = get_neighbours(row, col)
    seen.add((row, col))
    for r, c in neighbours:
        nr, nc = row+r, col+c
        if nr<0 or nr >= len(grid) or nc<0 or nc >= len(grid[0]):
            continue
        elif (nr, nc) in seen:
            continue

        for rinc, cinc in get_neighbours(nr, nc):
            if (nr+rinc, nc+cinc) == (row, col):
                break
        else:
            continue

        update_team(nr, nc, row, col)

        out = search2(nr, nc, (row, col))

search2(*start)
counts = [0, 0]
for row in teams:
    for t in row:
        if t != -1:
            counts[t] += 1
# make a guess at one of the options
# probably the smaller number
print(counts)