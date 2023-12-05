with open("22.txt", "r") as file:
    grid = []
    lines = file.readlines()
    for l in lines[:-2]:
        line = l[:-1]
        grid.append(line)
    dirs = lines[-1]



directions = []
num = ""
for char in dirs:
    if "0"<=char<="9":
        num += char
    else:
        inc = 1 if char == "R" else -1
        directions.append((int(num), inc))
        num = ""
print(directions)

def get_neighbours(row, col):
    neighbours = []
    right = (row, col+1)
    if col == len(grid[row])-1:
        new_col = 0
        while grid[row][new_col] == " ":
            new_col += 1
        right = (row, new_col)
    if grid[right[0]][right[1]] == ".":
        neighbours.append(right)
    else:
        neighbours.append(None)

    down = (row + 1, col)
    if row == len(grid) - 1 or col >= len(grid[down[0]]) or grid[down[0]][down[1]] == " ":
        new_row = 0
        while col >= len(grid[new_row]) or grid[new_row][col] == " ":
            new_row += 1
        down = (new_row, col)
    if grid[down[0]][down[1]] == ".":
        neighbours.append(down)
    else:
        neighbours.append(None)

    left = (row, col-1)
    if col == 0 or grid[left[0]][left[1]] == " ":
        new_col = len(grid[row])-1
        while grid[row][new_col] == " ":
            new_col -= 1
        left = (row, new_col)
    if grid[left[0]][left[1]] == ".":
        neighbours.append(left)
    else:
        neighbours.append(None)

    up = (row - 1, col)
    if row == 0 or col >= len(grid[up[0]]) or grid[up[0]][up[1]] == " ":
        new_row = len(grid)-1
        while col >= len(grid[new_row]) or grid[new_row][col] == " ":
            new_row -= 1
        up = (new_row, col)
    if grid[up[0]][up[1]] == ".":
        neighbours.append(up)
    else:
        neighbours.append(None)
    return neighbours



graph = {} # (row, col):  [right, down, left, up]

for row in range(len(grid)):
    for col in range(len(grid[row])):
        char = grid[row][col]
        if char == ".":
            neighbours = get_neighbours(row, col)
            graph[(row, col)] = neighbours


pos = (0, grid[0].index("."))
direction = 0

for amount, turn in directions:
    for _ in range(amount):
        next_pos = graph[pos][direction]
        if next_pos is None:
            break
        pos = next_pos

    direction = (direction + turn) % 4
    print(pos, direction)
print((pos[0]+1)*1000 + 4*(pos[1]+1) + direction)



