
with open("16.txt", "r") as file:
    pressures = {}

    graph = {}
    for l in file:
        line = l.strip().split()
        name = line[0]
        pressure = int(line[1])
        links = line[2:]
        if pressure > 0:
            pressures[name] = pressure
        graph[name] = links


def get_dist(a, b):
    nodes = [a]
    seen = {a}
    dist = 0
    while nodes:
        new_nodes = []
        for node in nodes:
            if node == b:
                return dist
            links = graph[node]
            for link in links:
                if link not in seen:
                    seen.add(link)
                    new_nodes.append(link)
        dist += 1
        nodes = new_nodes


pressure_arr = []
keys = list(pressures.keys())
distances = [[0 for _ in keys] for k in keys]
for i, a in enumerate(keys):
    pressure_arr.append(pressures[a])
    for j, b in enumerate(keys):
        distances[i][j] = get_dist(a, b)

print(keys)

start_distances = []
for i, name in enumerate(keys):
    start_distances.append((i, get_dist("AA", name)))




#         name    open    time
nodes = [(name,     0,   30-dist) for name, dist in start_distances]


memo = {}
def get_score(p1,  open, time):
    if time <= 0:
        return 0

    memo_find = memo.get((p1, open, time))
    if memo_find is not None:
        return memo_find

    result = 0
    if not ((1 << p1) & open):
        result = 0
        result = max(result, pressure_arr[p1] * (time - 1) + get_score(p1, open | (1 << p1), time - 1))
    for new_node, distance in enumerate(distances[p1]):
        if new_node == p1:
            continue
        result = max(result, get_score(new_node, open, time-distance))

    memo[(p1, open, time)] = result
    return result




results = [get_score(*node) for node in nodes]

print(max(results))
