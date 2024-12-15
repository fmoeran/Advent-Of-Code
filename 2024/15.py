# one of my favourite ones this year. Got to use a nice recursive block pushing algorithm
with open("15.txt", "r") as file:
    lines = [line.strip() for line in file]

dic = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}
replace = {"#": "##", "O": "[]", ".": "..", "@": "@."}

grid = []
for line in lines[:lines.index("")]:
    row = []
    for val in line:
        for item in replace[val]:
            row.append(item)
    grid.append(row)
directions = ""
for line in lines[lines.index("") + 1:]:
    directions += line

pos = (-1, -1)
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "@":
            pos = (r, c)
            break
grid[pos[0]][pos[1]] = "."
out = 0


def can_push_box(p1, d):
    if d == (0, 1) or d == (0, -1):
        dif = d[1]
        gaps = 0
        for v in grid[p1[0]][p1[1] + dif::dif]:
            if v == "#":
                break
            if v == ".":
                gaps += 1
        return gaps >= 1
    val = grid[p1[0]][p1[1]]
    if val == "#":
        return False
    elif val == ".":
        return True
    elif val == "[":
        p2 = (p1[0], p1[1] + 1)
    else:
        p2 = (p1[0], p1[1] - 1)
    n1 = (p1[0] + d[0], p1[1] + d[1])
    n2 = (p2[0] + d[0], p2[1] + d[1])

    return can_push_box(n1, d) and can_push_box(n2, d)


def push_box(p1, d):
    global grid
    if d == (0, 1) or d == (0, -1):
        dif = d[1]
        c = p1[1] + dif
        prev = grid[p1[0]][p1[1]]
        while prev != ".":
            prev, grid[p1[0]][c] = grid[p1[0]][c], prev
            c += dif
        grid[p1[0]][p1[1]] = "."
        return
    val = grid[p1[0]][p1[1]]
    if val == "#":
        return
    elif val == ".":
        return
    elif val == "[":
        p2 = (p1[0], p1[1] + 1)
    else:
        p2 = (p1[0], p1[1] - 1)
    n1 = (p1[0] + d[0], p1[1] + d[1])
    n2 = (p2[0] + d[0], p2[1] + d[1])

    push_box(n1, d)
    push_box(n2, d)
    grid[n1[0]][n1[1]] = grid[p1[0]][p1[1]]
    grid[n2[0]][n2[1]] = grid[p2[0]][p2[1]]
    grid[p1[0]][p1[1]] = "."
    grid[p2[0]][p2[1]] = "."


for direction in directions:
    d = dic[direction]
    np = (pos[0] + d[0], pos[1] + d[1])
    v = grid[np[0]][np[1]]

    if v == "#":
        continue
    if v in "[]":
        if can_push_box(np, d):
            push_box(np, d)
        else:
            continue

    grid[np[0]][np[1]] = "."
    pos = np

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "[":
            out += 100 * r + c
print(out)
