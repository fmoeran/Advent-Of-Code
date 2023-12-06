with open("16.txt", "r") as file:
    pressures = {}

    graph = {}
    for l in file:
        line = l.strip().split()
        name = line[0]
        pressure = int(line[1])
        links = line[2:]
        pressures[name] = pressure
        graph[name] = links

keys = list(pressures.keys())
pressure_arr = [pressures[key] for key in keys]

m = len(keys)

dist = [[float('inf') for i in keys] for j in keys]
for v in range(len(keys)):
    dist[v][v] = 0
for name, links in graph.items():
    v = keys.index(name)
    for link in links:
        w = keys.index(link)
        dist[v][w] = 1

for k in range(m):
    for i in range(m):
        for j in range(m):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

memo = {}


def get_score(p1, open, time, is_p2):
    if time <= 0:
        if is_p2:
            return get_score(0, open, 26, False)
        else:
            return 0

    memo_find = memo.get((p1, open, time, is_p2))
    if memo_find is not None:
        return memo_find

    result = 0
    if not ((1 << p1) & open) and pressure_arr[p1] != 0:
        result = 0
        result = max(result, pressure_arr[p1] * (time - 1) + get_score(p1, open | (1 << p1), time - 1, is_p2))
    for new_node, distance in enumerate(dist[p1]):
        if new_node == p1:
            continue
        result = max(result, get_score(new_node, open, time - distance, is_p2))

    memo[(p1, open, time, is_p2)] = result
    #print(result)
    return result


print(get_score(0, 0, 26, True))
