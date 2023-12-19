with open("18.txt", "r") as f:
    ops = [line.strip() for line in f]


dirs = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}

dirs2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# path
mn = [0, 0]
pos = [0, 0]
rows = {}
connections = {}
for op in ops:
    _1, _2, col = op.split()
    d = dirs2[int(col[-2])]
    n = int(col[2:7], 16)

    #d = dirs[_1]
    #n = int(_2)

    if d[0]:
        rows[pos[0]] = rows.get(pos[0], []) + [pos[1]]
        if len(rows[pos[0]])%2 == 0:
            connections[pos[0]] = connections.get(pos[0], []) + [(rows[pos[0]][-2], rows[pos[0]][-1])]

    pos[0] += d[0] * n
    pos[1] += d[1] * n

    if d[0]:
        rows[pos[0]] = rows.get(pos[0], []) + [pos[1]]
        if len(rows[pos[0]]) % 2 == 0:
            connections[pos[0]] = connections.get(pos[0], []) + [(rows[pos[0]][-2], rows[pos[0]][-1])]


walls = sorted(rows.items())
blocks = sorted(walls[0][1])
total = 0
t = 0
for i in range(1, len(walls)):

    width = 0
    for j in range(1, len(blocks), 2):
        width += blocks[j] - blocks[j-1] + 1
    height = walls[i][0] - walls[i-1][0] + 1
    total += width * height

    new_blocks = blocks[:]
    for block in walls[i][1]:
        if block in new_blocks:
            new_blocks.remove(block)
        else:
            new_blocks.append(block)

    new_blocks.sort()
    shared = 0
    start = 0
    for j in range(0, len(blocks), 2):
        a, b = blocks[j], blocks[j+1]
        for k in range(start, len(new_blocks), 2):
            c, d = new_blocks[k], new_blocks[k+1]
            if c > b:
                break
            if d < a:
                start = k
            x, y = max(a, c), min(b, d)
            shared += max(y-x+1, 0)

    blocks = new_blocks[:]
    total -= shared


print(total)
