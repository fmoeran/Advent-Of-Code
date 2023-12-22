# just please do not ask

with open("21.txt", "r") as f:
    grid = [line.strip() for line in f]

# goal = 64



goal = 26501365


def searchA(start):
    goal = 64
    nodes = [start]
    for step in range(goal):
        new_nodes = set()
        for node in nodes:
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nd = (node[0] + d[0], node[1] + d[1])
                if 0 <= nd[0] < len(grid) and nd[1] >= 0 and nd[1] < len(grid[0]):
                    if grid[nd[0]][nd[1]] != "#":
                        new_nodes.add(nd)
        nodes = list(new_nodes)
    print(len(nodes))


def bfB(start, goal):
    nodes = [start]
    counts = [1, 0]
    seen = [{start}, set()]
    for step in range(1, goal + 1):
        new_nodes = set()
        for node in nodes:
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nd = ((node[0] + d[0]), (node[1] + d[1]))

                if grid[nd[0] % len(grid)][nd[1] % len(grid)] != "#" and nd not in seen[step % 2]:
                    new_nodes.add(nd)
                    seen[step % 2].add(nd)
        nodes = list(new_nodes)
        counts[step % 2] += len(nodes)

    mxlayer = goal // 131
    a, b, c, d = 0, 0, 0, 0
    for node in seen[goal % 2]:
        dist = (abs(node[0] - start[0]), abs(node[1] - start[1]))
        layer = (dist[0] + start[0]) // 131 + (dist[1] + start[1]) // 131

        if layer < mxlayer - 1:
            a += 1
        elif layer == mxlayer - 1:
            b += 1
        elif layer >= mxlayer and (dist[0] + start[0]) // 131 and (dist[1] + start[1]) // 131:
            c += 1
        else:
            d += 1

    print(a, b, c, d)
    return counts[goal % 2]


def out_of_bounds(coord):
    return 0 > coord[0] or coord[0] >= len(grid) or coord[1] < 0 or coord[1] >= len(grid[0])


def get_pos_count(starts, remaining, check=lambda x: not out_of_bounds(x)):
    nodes = starts
    counts = [len(starts), 0]
    seen = [set(starts), set()]
    for step in range(1, remaining + 1):
        new_nodes = set()
        for node in nodes:
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nd = (node[0] + d[0], node[1] + d[1])
                if check(nd):
                    if grid[nd[0] % len(grid)][nd[1] % len(grid)] != "#" and nd not in seen[step % 2]:
                        new_nodes.add(nd)
                        seen[step % 2].add(nd)
        nodes = list(new_nodes)
        counts[step % 2] += len(nodes)

    return counts[remaining % 2]


def searchB(start):
    corners = [(0, 0), (0, len(grid[0]) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid[0]) - 1)]
    time_to_corners = 130

    time_across_garden = len(grid)
    total = 0
    evens = get_pos_count([start], 130)
    odds = get_pos_count([start], 131)
    remaining = goal - time_to_corners
    # num of layers not including last two layers
    layer_count = (remaining // time_across_garden)
    for l in range(layer_count):
        if (l + goal) % 2 == 0:
            total += max(1, 4 * l) * evens
        else:
            total += max(1, 4 * l) * odds
    print("+inner layers:", total)

    remaining -= (layer_count - 1) * time_across_garden
    outer_layer = layer_count  # second last layer
    inc = 0
    for corner in corners:
        inc += get_pos_count([corner], remaining + time_across_garden - 2) * (outer_layer - 1)



    print("+second last layer:", inc)
    total += inc

    # last layer & extra
    inc = 0
    outer_layer += 1  # last layer

    remaining = (goal - time_to_corners) % time_across_garden + time_across_garden
    # Just don't ask...
    # This is black magic now

    for corner in corners:
        inc += get_pos_count([corner], remaining - 2) * (outer_layer - 1)
        # extra
        inc += get_pos_count([corner], remaining - 2 - time_across_garden) * outer_layer

    print("+last and extra:", inc)
    total += inc

    inc = 0

    half = len(grid) // 2
    remaining = (goal - half - 1) % time_across_garden + time_across_garden

    inc += get_pos_count([(0, half)], remaining, lambda x: x[0] >= 0 and 0 <= x[1] < len(grid))
    inc += get_pos_count([(len(grid) - 1, half)], remaining, lambda x: x[0] < len(grid) and 0 <= x[1] < len(grid))
    inc += get_pos_count([(half, 0)], remaining, lambda x: 0 <= x[0] < len(grid) and 0 <= x[1])
    inc += get_pos_count([(half, len(grid) - 1)], remaining, lambda x: 0 <= x[0] < len(grid) and x[1] < len(grid))

    print("+peaks:", inc)
    total += inc

    print("total:", total)



s = (0, 0)

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "S":
            s = (r, c)
            break
    else:
        continue
    break

searchB(s)
