with open("16.txt", "r") as f:
    grid = [line.strip() for line in f]


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


mx = 0


def search(start, sd):
    searching = [(start, sd)]
    seen = set(searching)

    seen_pos = set()

    while searching:
        new_searching = []
        for pos, d in searching:
            if pos not in seen_pos:
                seen_pos.add(pos)
            np = (pos[0]+d[0], pos[1]+d[1])
            if np[0] < 0 or np[0] >= len(grid[0]) or np[1] < 0 or np[1] >= len(grid):
                continue
            else:
                if grid[np[0]][np[1]] != ".":
                    char = grid[np[0]][np[1]]

                    if char == "-":
                        if d[0]:
                            new_searching.append((np, (0, 1)))
                            new_searching.append((np, (0, -1)))
                        elif d[1]:
                            new_searching.append((np, d))
                    elif char == "|":

                        if d[1]:
                            new_searching.append((np, (1, 0)))
                            new_searching.append((np, (-1, 0)))
                        elif d[0]:
                            new_searching.append((np, d))
                    elif char == "/":
                        if d[0]:
                            new_searching.append((np, (0, -d[0])))
                        elif d[1]:
                            new_searching.append((np, (-d[1], 0)))
                    elif char == "\\":
                        if d[0]:
                            new_searching.append((np, (0, d[0])))
                        elif d[1]:
                            new_searching.append((np, (d[1], 0)))
                else:
                    new_searching.append((np, d))
        searching = []
        for s in new_searching:
            if s not in seen:
                seen.add(s)
                searching.append(s)
    global mx
    mx = max(len(seen_pos)-1, mx)




for row in range(len(grid)):
    search((row, -1), (0, 1))
    search((row, len(grid[0])), (0, -1))


for col in range(len(grid[0])):
    search((-1, col), (1, 0))
    search((len(grid), col), (-1, 0))

print(mx)





