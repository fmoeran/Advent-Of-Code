# First properly NP-hard problem!
# The previous NPHs were special cases that made them P
# But so far I can't see anyone on reddit who doesn't think this one rlly is NPH
# The only trick was to contract the graph a bit


import sys
from functools import cache

sys.setrecursionlimit(10000)

with open("23.txt", "r") as f:
    arr = [line.strip() for line in f]


def get_difs(node):
    return [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if arr[node[0]][node[1]] == "^":
        return [(-1, 0)]
    elif arr[node[0]][node[1]] == ">":
        return [(0, 1)]
    elif arr[node[0]][node[1]] == "v":
        return [(1, 0)]
    elif arr[node[0]][node[1]] == "<":
        return [(0, -1)]
    else:
        return [(-1, 0), (0, 1), (1, 0), (0, -1)]


def in_bounds(node):
    return 0 <= node[0] < len(arr) and 0 <= node[1] < len(arr[0])


def search(node, end, seen):
    # bfs
    if node == end:
        return 0
    out = 0
    mxpos = node
    for d in get_difs(node):
        nd = (node[0] + d[0], node[1] + d[1])
        if in_bounds(nd) and nd not in seen and arr[nd[0]][nd[1]] != '#':
            seen.add(nd)
            res = search(nd, end, seen) + 1
            if res > out:
                out = res
                mxpos = res

            seen.remove(nd)

    if mxpos == node:
        return -100000

    return out


def is_junction(node):
    if node == (0, 1) or node == (len(arr) - 1, len(arr) - 2):
        return True
    count = 0
    for d in get_difs(node):
        nd = (node[0] + d[0], node[1] + d[1])
        if in_bounds(nd) and arr[nd[0]][nd[1]] in "^v><":
            count += 1
    if count >= 3:
        return True
    return False


start = (0, 1)
end = (len(arr) - 1, len(arr) - 2)

junctions = []

for row in range(len(arr)):
    for col in range(len(arr[0])):
        if is_junction((row, col)):
            junctions.append((row, col))

graph = [[] for _ in junctions]


def create_graph(root):
    root_node = junctions[root]

    nodes = [(root_node, root_node, 0)]

    while nodes:
        node, prev, dist = nodes.pop()
        if node != root_node and is_junction(node):
            jind = junctions.index(node)
            graph[root].append((jind, dist))
            if len(graph[jind]) == 0:
                create_graph(jind)
        else:
            for d in get_difs(node):
                nd = (node[0] + d[0], node[1] + d[1])
                if nd != prev and in_bounds(nd) and arr[nd[0]][nd[1]] != '#':
                    nodes.append((nd, node, dist + 1))


create_graph(0)




# uses memo and uses a bitmask instead of a set for seen
@cache
def searchB(node, end, seen):
    # bfs
    if node == len(junctions)-1:
        return 0
    out = 0
    mxpos = node
    for nd, weight in graph[node]:
        if (1 << nd) & seen == 0:
            seen ^= 1 << nd
            res = searchB(nd, end, seen) + weight
            if res > out:
                out = res
                mxpos = res

            seen ^= 1 << nd

    if mxpos == node:
        return -100000

    return out


seen = 1

# kinds slow lol I'll find a way to speed it up
print(searchB(0, len(junctions)-1, seen))
