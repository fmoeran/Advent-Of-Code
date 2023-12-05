blocked = set()

with open("14.txt", "r") as file:
    for l in file:
        line = l.strip().split(" -> ")
        coords = []
        for pair in line:
            coords.append(tuple(map(int, pair.split(","))))

        for i, coord in enumerate(coords[:-1]):
            ncoord = coords[i+1]
            if coord[0] < ncoord[0]:
                dif = (1, 0)
            elif coord[0] > ncoord[0]:
                dif = (-1, 0)
            elif coord[1] < ncoord[1]:
                dif = (0, 1)
            else:
                dif = (0, -1)
            while coord != ncoord:
                blocked.add(coord)
                coord = (coord[0]+dif[0], coord[1]+dif[1])
            blocked.add(coord)

low = float("-inf")

for x, y in blocked:
    if y > low:
        low = y


start = (500, 0)


def simulate():
    pos = start
    while pos[1] <= low:
        if (pos[0], pos[1]+1) not in blocked:
            pos = (pos[0], pos[1]+1)
        elif (pos[0]-1, pos[1]+1) not in blocked:
            pos = (pos[0]-1, pos[1]+1)
        elif (pos[0]+1, pos[1]+1) not in blocked:
            pos = (pos[0] + 1, pos[1] + 1)
        else:
            break
    return pos

running = True
count = 0
while running:
    count += 1
    pos = simulate()
    blocked.add(pos)
    if pos == start:
        running = False


print(count)

