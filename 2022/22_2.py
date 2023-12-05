with open("22.txt", "r") as file:
    lines = file.readlines()


incs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dirs = lines.pop().strip()
lines.pop()

directions = []
num = ""
for char in dirs:
    if "0" <= char <= "9":
        num += char
    else:
        new_dir = 1 if char == "R" else -1
        directions.append((int(num), new_dir))
        num = ""
directions.append((int(num), 0))


def get_neighbours(row, col):
    neighbours = []

    for rinc, cinc in incs:
        nrow, ncol = (row + rinc) % maxrow, (col + cinc) % maxcol
        while (nrow, ncol) not in points:
            nrow, ncol = (nrow + rinc) % maxrow, (ncol + cinc) % maxcol
        neighbours.append((nrow, ncol))
    return neighbours


grid = []
for line in lines:
    grid.append(line[:-1])

points = set()
for row, r in enumerate(grid):
    for col, item in enumerate(r):
        if item != " ":
            points.add((row, col))

maxrow, maxcol = len(grid), len(max(grid, key=lambda x: len(x)))

graph = {}
for row, col in points:
    if grid[row][col] != " ":
        neighbours = get_neighbours(row, col)
        graph[(row, col)] = neighbours



#  10
#  2
# 43
# 5

sides_positions = [[None, 1, 0],
                   [None, 2, None],
                   [   4, 3, None],
                   [   5, None, None]]
side_size = 50
sides = [[] for _ in range(6)]
for row in range(len(sides_positions)):
    for col in range(len(sides_positions[0])):
        if sides_positions[row][col] is None:
            continue
        srow, scol = row*side_size, col*side_size
        erow, ecol = srow + side_size, scol + side_size
        ind = sides_positions[row][col]
        side = sides[ind]
        side.append(tuple([(r, ecol-1) for r in range(srow, erow)]))
        side.append(tuple([(erow-1, c) for c in range(scol, ecol)]))
        side.append(tuple([(r, scol) for r in range(srow, erow)]))
        side.append(tuple([(srow, c) for c in range(scol, ecol)]))
        sides[ind] = tuple(side)


# (num face to link to, side of face to link to)
links = {sides[0]: [sides[3][0][::-1], sides[2][0], sides[1][0], sides[5][1]],
         sides[1]: [sides[0][2], sides[2][3], sides[4][2][::-1], sides[5][2]],
         sides[2]: [sides[0][1], sides[3][3], sides[4][3], sides[1][1]],
         sides[3]: [sides[0][0][::-1], sides[5][0], sides[4][0], sides[2][1]],
         sides[4]: [sides[3][2], sides[5][3], sides[1][2][::-1], sides[2][2]],
         sides[5]: [sides[3][1], sides[0][3], sides[1][3], sides[4][1]]}


for face, ls in links.items():
    for direction, new_side in enumerate(ls):
        for p1, p2 in zip(face[direction], new_side):

            graph[p1][direction] = p2


point = (0, grid[0].index("."))
inc = 0
for amount, turn in directions:
    for _ in range(amount):
        next_point = graph[point][inc]
        if grid[next_point[0]][next_point[1]] == "#":
            break
        old_point = point
        point = next_point
        if abs(point[0]-old_point[0]) + abs(point[1]-old_point[1]) > 1:
            print("    changed")
            if graph.get((point[0], point[1]-1)) is None:
                inc = 0
            elif graph.get((point[0]-1, point[1])) is None:
                inc = 1
            elif graph.get((point[0], point[1]+1)) is None:
                inc = 2
            elif graph.get((point[0]+1, point[1])) is None:
                inc = 3

    inc = (inc + turn) % 4


row = point[0] + 1
col = point[1] + 1
print(row * 1000 + col * 4 + inc)







