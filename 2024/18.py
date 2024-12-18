# easy one today. I know Eric likes to add randomly easy and hard ones throughout,
# quite glad actually I was not prepared to have another 2 hour coding session like yesterday.
# A bit sad that BF worked today, would have really liked a dynamic graph sort where whenever we add a
# memory bit, we only have to check a smaller search space by using the previous searches but that'll take way longer
# to make

with open("18.txt", "r") as file:
    blocks = [tuple(map(int, line.strip().split(","))) for line in file]

mx = 71
# mx = 7

N = 1024
# N = 12


end = (mx - 1, mx - 1)

grid = [[False] * mx for _ in range(mx)]


# for block in blocks[:N]:
#     grid[block[0]][block[1]] = True

def neighbours(row, col):
    out = []
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = row + d[0]
        nc = col + d[1]
        if 0 <= nr < mx and 0 <= nc < mx and not grid[nr][nc]:
            out.append((nr, nc))
    return out


def exists():
    seen = [[False] * mx for _ in range(mx)]
    seen[0][0] = True
    dist = 0
    nodes = [(0, 0)]
    while nodes:
        new_nodes = []
        for node in nodes:
            if node == end:
                return True
            for neigh in neighbours(*node):
                if seen[neigh[0]][neigh[1]]:
                    continue
                seen[neigh[0]][neigh[1]] = True
                new_nodes.append(neigh)
        nodes = new_nodes
        dist += 1
    return False


for ind, block in enumerate(blocks):
    grid[block[0]][block[1]] = True
    if not exists():
        print(block[0], block[1], sep="")
        break
