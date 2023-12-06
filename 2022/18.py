blocks = set()

with open("18.txt", "r") as file:
    for l in file:
        line = tuple(map(int, l.strip().split(",")))
        blocks.add(line)


def get_neighbours(pos):
    p = list(pos)
    neighbours = []
    for i in range(3):
        p[i] += 1
        neighbours.append(tuple(p))
        p[i] -= 2
        neighbours.append(tuple(p))
        p[i] += 1
    return neighbours


maxs = [max(blocks, key=lambda x: x[i]) for i in range(3)]
maxs = tuple([x[i]+1 for i, x in enumerate(maxs)])
mins = [min(blocks, key=lambda x: x[i]) for i in range(3)]
mins = tuple([x[i]-1 for i, x in enumerate(mins)])




def flood_fill(pos):
    global blocks
    blocks.add(pos)
    nodes = [pos]
    while nodes:
        node = nodes.pop()
        neighbours = get_neighbours(node)

        for n in neighbours:
            for i in range(3):
                if n[i]>maxs[i] or n[i]<mins[i]:
                    break
            else:
                if n in blocks:
                    continue
                blocks.add(n)
                nodes.append(n)





neighbouring = set()
for pos in blocks:
    for n in get_neighbours(pos):
        if n in blocks:
            neighbouring.add((pos, n))

original = len(blocks)*6-len(neighbouring)


flood_fill(maxs)
print(maxs)
neighbouring = set()
for pos in blocks:
    for n in get_neighbours(pos):
        if n in blocks:
            neighbouring.add((pos, n))

difs = [maxs[i]-mins[i]+1 for i in range(3)]
sa = difs[0]*difs[1]*2 + difs[2]*difs[1]*2 + difs[0]*difs[2]*2

new_total = len(blocks)*6-len(neighbouring) - sa
print(original, new_total)
print(original-new_total)