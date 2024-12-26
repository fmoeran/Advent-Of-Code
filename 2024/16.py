# quite disappointed I didn't have to use anything more clever than just keeping track of all possible previous nodes
# during a dijkstras, but oh well it works (slowly)!
# UPDATE: added backtracking to improve speed.
from heapq import heapify, heappop, heappush
from collections import defaultdict

with open("16.txt", "r") as file:
    grid = [line.strip() for line in file]

start, end = (-1, -1), (-1, -1)
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "S":
            start = (r, c)
        if val == "E":
            end = (r, c)

difs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

heap = [(0, start, 0)]

scores = defaultdict(lambda: 1000000000000)
scores[(start, 0)] = 0

heapify(heap)
bscore = 1000000000000000
while heap:
    score, pos, d_ind = heappop(heap)
    if pos == end:
        bscore = min(score, bscore)
    d = difs[d_ind]
    npos = (pos[0] + d[0], pos[1] + d[1])
    if grid[npos[0]][npos[1]] != "#":
        if scores[(npos, d_ind)] >= score + 1:
            heappush(heap, (score + 1, npos, d_ind))
            scores[(npos, d_ind)] = score + 1

    for nd in [(d_ind + 1) % 4, (d_ind - 1) % 4]:
        if scores[(pos, nd)] >= score + 1000:
            heappush(heap, (score + 1000, pos, nd))
            scores[(pos, nd)] = score + 1000


def backtrack(pos, d_ind):
    out = {pos}
    d = difs[d_ind]
    npos = (pos[0] - d[0], pos[1] - d[1])
    current_score = scores[(pos, d_ind)]
    if grid[npos[0]][npos[1]] != '#':
        if scores[(npos, d_ind)] == current_score - 1:
            out = out.union(backtrack(npos, d_ind))
    for nd in [(d_ind + 1) % 4, (d_ind - 1) % 4]:
        if scores[(pos, nd)] == current_score - 1000:
            out = out.union(backtrack(pos, nd))
    return out


print(bscore)
for d in range(4):
    if scores[(end, d)] == bscore:
        b = backtrack(end, d)
        print(len(b))
