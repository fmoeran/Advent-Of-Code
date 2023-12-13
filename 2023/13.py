# Got rank 77 today!

with open("13.txt", "r") as f:
    arr = [line.strip() for line in f]
grids = [[] ]
for line in arr:
    if not line:
        grids.append([])
    else:
        grids[-1].append(line)


def get_dif(s1, s2):
    total = 0
    for a, b in zip(s1, s2):
        if a != b:
            total += 1
    return total


def get_reflection(grid):
    rows, cols = 0, 0
    for row in range(len(grid)-1):
        dif = 0
        l, r = row, row+1
        while l>=0 and r < len(grid):
            dif += get_dif(grid[l], grid[r])
            l -= 1
            r += 1
        if dif == 1:
            return row+1, 0

    def get_col(c):
        return [r[c] for r in grid]

    for col in range(len(grid[0])-1):
        l, r = col, col+1
        dif = 0
        while l >= 0 and r < len(grid[0]):
            dif += get_dif(get_col(l), get_col(r))
            l -= 1
            r += 1
        if dif == 1:
            return 0, col + 1

total = 0
for grid in grids:
    r, c = get_reflection(grid)
    total += 100*r + c
print(total)

