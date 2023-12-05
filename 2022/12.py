import heapq

with open("12.txt", "r") as file:
    grid = []
    for l in file:
        grid.append(list(l.strip()))

start, end = None, None
for row, r in enumerate(grid):
    for col, char in enumerate(r):
        if char == "S":
            start = (row, col)
        if char == "E":
            end = (row, col)
grid[start[0]][start[1]] = "a"
grid[end[0]][end[1]] = "z"


def get_neighbours(row, col):
    neighbours = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
    new = []
    for r, c in neighbours:
        if 0<=r<len(grid) and 0<=c<len(grid[0]):
            new.append((r, c))
    return new

def get_dist(row, col):
    return abs(end[0]-row)+abs(end[1]-col)



def get_shortest(start, end):
    nodes = [(0, start)]
    heapq.heapify(nodes)
    seen = set()


    while nodes:
        dist, (row, col) = heapq.heappop(nodes)
        if (row, col) in seen:
            continue
        seen.add((row, col))
        if (row, col) == end:
            break
        val = grid[row][col]
        neighbours = get_neighbours(row, col)
        for nrow, ncol in neighbours:
            new_val = grid[nrow][ncol]
            if ord(val)+1 >= ord(new_val):
                if (nrow, ncol) in seen:
                    continue

                heapq.heappush(nodes, (dist+1, (nrow, ncol)))
    if (row, col) == end:
        return dist
    else:
        return float("inf")


mini = float("inf")
for row in range(len(grid)):
    for col in range(len(grid)):
        if grid[row][col] == "a":
            dist = get_shortest((row, col), end)
            if dist < mini:
                mini = dist
                print(dist)
                print(row, col)


