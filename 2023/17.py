# just dijkstra, It's pretty slow and A* is definitely better,
# but this was quick to make!

from heapq import heapify, heappush, heappop

with open("17.txt", "r") as f:
    arr = [line.strip() for line in f]


def search(sr, sc):
    q = [(0, (sr, sc), (1, 0), 0), (0, (sr, sc), (0, 1), 0)]
    end = (len(arr) - 1, len(arr[0]) - 1)
    heapify(q)
    seen = set()
    seen.add(((sr, sc), (1, 0), 0))
    seen.add(((sr, sc), (0, 1), 0))

    def add(heat, pos, d, straight):
        if pos[0] < 0 or pos[0] >= len(arr) or pos[1] < 0 or pos[1] >= len(arr[0]):
            return
        if (pos, d, straight) in seen:
            return

        heappush(q, (heat + int(arr[pos[0]][pos[1]]), pos, d, straight))
        seen.add((pos, d, straight))

    while q:

        heat, pos, d, straight = heappop(q)
        if pos == end and straight >= 4:
            print(heat)
            return
        row, col = pos

        if straight < 10:
            np = (row + d[0], col + d[1])
            add(heat, np, d, straight + 1)
        if straight >= 4:
            add(heat, (row + d[1], col + d[0]), (d[1], d[0]), 1)
            add(heat, (row - d[1], col - d[0]), (-d[1], -d[0]), 1)


search(0, 0)
