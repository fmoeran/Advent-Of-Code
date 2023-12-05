


algorithm = ""
image = {}
n = 0

default = "."

with open("20.txt", "r") as f:
    algorithm = f.readline().strip()

    for row, line in enumerate(f.readlines()[1:]):
        for col, c in enumerate(line.strip()):
            image[(row, col)] = c


def get_neighbours(coord):
    out = []
    for r in range(-1, 2):
        for c in range(-1, 2):
            out.append((coord[0]+r, coord[1]+c))
    return out

def step():
    global image, default
    seen = set()
    new_image = {}
    for (key, val) in image.items():
        for center in get_neighbours(key):
            if center not in seen:
                seen.add(center)

                val = 0
                power = 1<<8
                for pos in get_neighbours(center):
                    if image.get(pos, default) == "#":
                        val += power
                    power >>= 1
                new_image[center] = algorithm[val]
    image = new_image
    if default == "#": default = "."
    else: default = "#"


for i in range(50):
    step()
    print(i)

total = 0
for (coord, val) in image.items():
    if val == "#":
        total += 1

print(total)




