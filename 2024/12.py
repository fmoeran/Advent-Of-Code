#WOW i really struggled on the second part. I had a strategy that was SO CLOSE to working
# it passed every test they gave but failed the real thing and it took me ages to find a test case that didnt work
with open("12.txt", "r") as file:
    grid = [line.strip() for line in file]

seen = [[False] * len(line) for line in grid]

registered = [[[] for v in line] for line in grid]

def neighbours(row, col):
    out = []
    for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            out.append((nr, nc))
    return out

# used in part A

def get_ap(row, col):
    seen[row][col] = True
    area = 1
    neighs = neighbours(row, col)
    perim = 4 - len(neighs)
    for nr, nc in neighs:
        if grid[nr][nc] == grid[row][col] and not seen[nr][nc]:
            res = get_ap(nr, nc)
            area += res[0]
            perim += res[1]
        elif grid[nr][nc] != grid[row][col]:
            perim += 1
    return area, perim

# part B

def get_sides(row, col):
    sides = []
    for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if (not (0 <= nr < len(grid) and 0 <= nc < len(grid[0]))) or grid[nr][nc] != grid[row][col]:
            sides.append((dr, dc))
    return sides


def get_as(row, col):
    seen[row][col] = True
    area = 1
    neighs = neighbours(row, col)
    sides = get_sides(row, col)
    t_sides = 0

    for side in sides:
        already_r = False
        for d in [(side[1], side[0]), (-side[1], -side[0])]:
            if already_r: break
            x = (row, col)
            while side in get_sides(*x):
                x = (x[0] + d[0], x[1] + d[1])
                if not (0 <= x[0] < len(grid) and 0 <= x[1] < len(grid[0])):
                    break
                if grid[x[0]][x[1]] != grid[row][col]:
                    break
                if side in registered[x[0]][x[1]]:
                    already_r = True
                    break
        if not already_r:
            registered[row][col].append(side)
            t_sides += 1

    for nr, nc in neighs:
        if grid[nr][nc] == grid[row][col] and not seen[nr][nc]:
            res = get_as(nr, nc)
            area += res[0]
            t_sides += res[1]
    return area, t_sides


t = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if seen[r][c]:
            continue
        res = get_as(r, c)
        print(res, grid[r][c])
        t += res[0] * res[1]
print(t)
