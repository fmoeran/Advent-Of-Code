

dirs = {">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0)}


horizontals = []
verticals = []

with open("24.txt", "r") as file:
    lines = file.readlines()
    mincol, maxcol = 0, len(lines[0])-2
    minrow, maxrow = 0, len(lines)-1
    for row in range(minrow+1, maxrow):
        for col in range(mincol+1, maxcol):
            item = lines[row][col]
            if item != ".":
                position = (row, col)
                direction = dirs[item]
                if item in "><":
                    horizontals.append((position, direction))
                else:
                    verticals.append((position, direction))

end = (maxrow, maxcol-1)
start = (minrow, mincol+1)

def add_pair(a, b):
    return tuple([a[0] + b[0], a[1] + b[1]])

def get_neighbours(row, col):
    neighbours = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    new_neighbours = [n for n in neighbours if (minrow<n[0]<maxrow and mincol<n[1]<maxcol) or n == end or n == start]
    new_neighbours.append((row, col))
    return new_neighbours

def update(ls):
    new_ls = []
    for position, direction in ls:
        new_position = list(add_pair(position, direction))
        if new_position[0] == maxrow:
            new_position[0] = minrow+1
        elif new_position[0] == minrow:
            new_position[0] = maxrow-1
        elif new_position[1] == maxcol:
            new_position[1] = mincol+1
        elif new_position[1] == mincol:
            new_position[1] = maxcol-1
        new_ls.append((tuple(new_position), direction))
    return new_ls

vertical_steps = []
horizontal_steps = []

for i in range(maxrow-minrow-1):
    verticals = update(verticals)
    vertical_steps.append(set(map(lambda x: x[0], verticals)))

for i in range(maxcol-mincol-1):
    horizontals = update(horizontals)
    horizontal_steps.append(set(map(lambda x: x[0], horizontals)))


def get_dist(start, end, min):
    positions = {start}
    minute = min

    while positions:
        if end in positions:
            break
        cur_hor = horizontal_steps[minute%len(horizontal_steps)]
        cur_ver = vertical_steps[minute%len(vertical_steps)]

        new_positions = set()
        for position in positions:
            neighbours = get_neighbours(*position)
            for n in neighbours:
                if n not in cur_hor and n not in cur_ver:
                    new_positions.add(n)
        positions = new_positions
        minute += 1
    return minute

d1 = get_dist(start, end, 0)
print(d1)
d2 = get_dist(end, start, d1)
print(d2)
d3 = get_dist(start, end, d2)
print(d3)




