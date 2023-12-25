# fun question! Woke up a bit later cause it's christmas! Not sure if I would have figured out a deterministic
# solution to this but a monte carlo search works very well cause a random path between two nodes has a 50% chance to
# contain one of the 3 cut nodes but a far lower chance for any of the others in fact just running the MC 100 times
# almost always gives the right answer (I ran it 10k times to make sure lol)
import random

with open("25.txt", "r") as f:
    arr = [line.strip() for line in f]

graph = {}

for line in arr:
    a, links = line.split(": ")
    links = links.split(" ")
    for b in links:
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]


def get_comp_size(root, banned):
    """
    assuming we have pruned off the correct edges, this returns the size of on of the two components
    """
    nodes = [root]
    seen = {root}
    while nodes:
        new_nodes = []
        for node in nodes:
            for neighbour in graph[node]:
                if neighbour in seen or (node, neighbour) in banned or (neighbour, node) in banned:
                    continue
                seen.add(neighbour)
                new_nodes.append(neighbour)
        nodes = new_nodes
    return len(seen)


def get_path(start, end):
    """
    returns the shortest path between start and end
    The solution doesn't NEED the shortest path (in fact it might be better random) but each cycle is quicker if we do
    """
    prev = {start: start}
    nodes = [start]
    seen = {start}
    while nodes:
        new_nodes = []
        for node in nodes:
            for neighbour in graph[node]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                prev[neighbour] = node
                new_nodes.append(neighbour)
        nodes = new_nodes

    if prev.get(end) is None:
        return None

    path = []
    node = end
    while node != start:
        path.append(node)
        node = prev[node]
    path.append(start)
    return path[::-1]


uses = {}
for _ in range(100): # higher range means more likely to be correct
    a, b = random.sample(list(graph.keys()), 2)
    path = get_path(a, b)
    for i in range(len(path) - 1):
        edge = tuple(sorted([path[i], path[i + 1]]))
        uses[edge] = uses.get(edge, 0) + 1


# the three most used edges will be the three we need to cut
s_uses = sorted(uses.items(), key=lambda x: x[1], reverse=True)

banned = [p[0] for p in s_uses[:3]]

# get the size of each sets
s1, s2 = get_comp_size(banned[0][0], banned), get_comp_size(banned[0][1], banned)
print(s1+s2 == len(graph))
print(s1*s2)
