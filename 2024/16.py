# quite disappointed I didn't have to use anything more clever than just keeping track of all possible previous nodes
# during a dijkstras, but oh well it works (slowly)!
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

prevs = defaultdict(lambda: set())

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
            if scores[(npos, d_ind)] == score+1:
                for val in prevs[(pos, d_ind)]:
                    prevs[(npos, d_ind)].add(val)
            else:
                prevs[(npos, d_ind)] = prevs[(pos, d_ind)].copy()
            prevs[(npos, d_ind)].add(pos)
            heappush(heap, (score + 1, npos, d_ind))
            scores[(npos, d_ind)] = score + 1

    for nd in [(d_ind + 1) % 4, (d_ind - 1) % 4]:
        if scores[(pos, nd)] >= score + 1000:
            if scores[(pos, nd)] == score+1000:
                for val in prevs[(pos, d_ind)]:
                    prevs[(pos, nd)].add(val)
            else:
                prevs[(pos, nd)] = prevs[(pos, d_ind)].copy()
            prevs[(pos, nd)].add(pos)
            heappush(heap, (score + 1000, pos, nd))
            scores[(pos, nd)] = score + 1000

print(bscore)
best = set()
for d in range(4):
    if scores[(end, d)] == bscore:
        for p in prevs[(end, d)]:
            best.add(p)
print(len(best)+1)
