with open("23.txt", "r") as file:
    elves = set()
    lines = file.readlines()
    for row, line in enumerate(lines):
        for col, char in enumerate(line.strip()):
            if char == "#":
                elves.add((row, col))

neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def north_check(row, col):
    return (row-1, col-1) not in elves and (row-1, col) not in elves and (row-1, col+1) not in elves
def south_check(row, col):
    return (row+1, col-1) not in elves and (row+1, col) not in elves and (row+1, col+1) not in elves
def west_check(row, col):
    return (row - 1, col - 1) not in elves and (row, col - 1) not in elves and (row + 1, col - 1) not in elves
def east_check(row, col):
    return (row-1, col+1) not in elves and (row, col+1) not in elves and (row+1, col+1) not in elves

checks = [(north_check, (-1, 0)), (south_check, (1, 0)), (west_check, (0, -1)), (east_check, (0, +1))]

def get_next_pos(row, col):
    for r, c in neighbours:
        nrow, ncol = row+r, col+c
        if (nrow, ncol) in elves:
            break
    else:
        return row, col
    for i in range(4):
        check, (nrow, ncol) = checks[i]
        if check(row, col):
            return nrow+row, ncol+col

    return row, col

def step():
    global elves, checks
    move_positions = set()
    doubles = set()
    for row, col in elves:
        next_pos = tuple(get_next_pos(row, col))
        if next_pos not in move_positions:
            move_positions.add(next_pos)
        else:
            doubles.add(next_pos)
    out = set()
    changed = False
    for row, col in elves:
        next_pos = tuple(get_next_pos(row, col))
        if next_pos in doubles:
            nrow, ncol = row, col
        else:
            nrow, ncol = next_pos
        out.add((nrow, ncol))
        if nrow != row or ncol != col:
            changed = True
    if not changed:
        return True

    elves = out
    checks.append(checks.pop(0))
count = 0
while True:
    count += 1
    if step():
        print(count)
        break

# maxrow = max(elves, key=lambda x: x[0])[0]
# minrow = min(elves, key=lambda x: x[0])[0]
# maxcol = max(elves, key=lambda x: x[1])[1]
# mincol = min(elves, key=lambda x: x[1])[1]
# total = 0
# for row in range(minrow, maxrow+1):
#     for col in range(mincol, maxcol+1):
#         if (row, col) not in elves:
#             total += 1
# print(total)

